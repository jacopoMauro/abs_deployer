"""
Usage: abs_deployer.py [<options>] <abs program file>
  Options:
    -o, --ofile: file where to save the output
    -v, --verbose
    -k, --keep: keep temp files

It requires the installation of zephyrus2 available from git@bitbucket.org:jacopomauro/zephyrus2.git    

Limitations:
  - the definition of the deployment components need to be done in just on step
    calling the setInstanceDescriptions on an object denoted as cloudProvider
   
Scenarios name have to differ from DC names

Requirements:
  Python packages
   - toposort https://pypi.python.org/simple/topsort/
   - zephyrus2 git@bitbucket.org:jacopomauro/zephyrus2.git    
"""

# TODO: error if cycle is detected


import json
import uuid
import re
from subprocess import Popen
import sys, getopt
import os
import logging as log
import signal
import psutil
import copy
from antlr4 import *
import zephyrus2

import settings
import code_generation
import decl_spec_lang.decl_spec_lang as decl_spec_lang
import ABS.abs_extractor as abs_extractor

DEVNULL = open(os.devnull, 'wb')

# List of the temp files.
TMP_FILES = []

# List of the running solvers.
RUNNING_SOLVERS = []

# If KEEP, don't delete temporary files.
KEEP = False

#log.basicConfig(filename='example.log',level=log.DEBUG)
#log.basicConfig(level=log.DEBUG)

def usage():
  """Print usage"""
  print(__doc__)


def remove_dots(obj):
  """
  Keeps only the part of the string after the dot to a json object
  """
  if isinstance(obj, basestring):
    return obj.rsplit('.',1)[-1]
  elif isinstance(obj, dict):
    new = {}
    for k in obj.keys():
      if isinstance(k, basestring):
        new[k.rsplit('.',1)[-1]] = remove_dots(obj[k])
      else:
        new[k] = remove_dots(obj[k])
    return new
  elif isinstance(obj,list):
    return map(remove_dots,obj)
  else:
    return obj
  

def read_json(json_file): 
  json_data = open(json_file)
  data = json.load(json_data)
  json_data.close()
  return data


def send_signal_proc(signal, proc):
  """
  Sends the specified signal to the process, and to all its children.
  """
  if proc.poll() is None:
    for p in proc.children(recursive = True):
      try:
        p.send_signal(signal)
      except psutil.NoSuchProcess:
        pass
    try:
      proc.send_signal(signal)
    except psutil.NoSuchProcess:
      pass


def clean():
  """
  Utility for (possibly) cleaning temporary files and killing the solvers 
  processes at the end of the solving process (even when the termination is 
  forced externally).
  """
  global RUNNING_SOLVERS
  for solver in RUNNING_SOLVERS:
    send_signal_proc(signal.SIGKILL, solver)
  # Possibly remove temporary files.
  if not KEEP:
    for f in TMP_FILES:
      if os.path.exists(f):
        os.remove(f)


def get_abs_names(data):
  """Extract from the json generated parsing the ABS the names of the classes, resouces, and interfaces"""
  classes = {}
  resources = set([])
  interfaces = set([])
  
  for i in data["classes"]:
    classes[i["name"]] = []
    for j in i["activates"]:
      if len(j["scenarios"]) == 0:
        classes[i["name"]].append(settings.DEFAULT_SCENARIO_NAME)
      else:
        classes[i["name"]].append(j["scenarios"][0])
      
      for k in j["cost"].keys():
        resources.add(k)
  
  for i in data["hierarchy"]:
    for j in data["hierarchy"][i]:
      interfaces.add(j)
    
  return (classes,resources,interfaces)


def generate_zep_input_from_annotations(data):
  """
  Generate the partial input for zephyrus starting from the json internal
  representation extracted from the abs program.
  Note that the names can not contain a '.' that in the specification language
  has its own meaning
  """

  zep = {
    "components" : {},
    "locations" : {}
    }
   
  for i in data["classes"]:
    component_name = i["name"]   
    for j in i["activates"]:
      comp = {
            "provides" : [ {} ],
            "requires" : {},
            "resources" : {}}
             
      # handle provide-ports
      if component_name in data["hierarchy"]:
        comp["provides"][0]["ports"] = data["hierarchy"][component_name]
      else:
        log.critical("Component " + component_name + "not present in hierarchy")
        exit(1)
      comp["provides"][0]["num"] =  j["provide"]
        
      # handle require-ports
      for k in j["sig"]:
        if k["type"] == "require" or k["type"] == "list":
          comp["requires"][k["value"]] = k["arity"]
      
      # handle resources
      comp["resources"].update(j["cost"])
      
      # decide the name            
      if len(j["scenarios"]) > 1:
        log.critical("In internal json scenarios has more than one element")
        log.critical("Exiting")
        sys.exit(1)
      elif len(j["scenarios"]) == 0:
        name = settings.DEFAULT_SCENARIO_NAME + settings.SEPARATOR + component_name
      else:
        name = j["scenarios"][0] + settings.SEPARATOR + component_name
      
      zep["components"][name] = comp
  return zep


def initialDC(annotation):
  """
  Creates a new type of DC for every initially available DC
  It takes the annotation in json format.
  It returns the data to include in zephyrus input and the maps between the DC
  components and its real name 
  """
  zep = {}
  dc_into_name = {}
  name_into_dc = {}
  
  for i in annotation["DC"]:
    name = settings.SEPARATOR + uuid.uuid4().hex
    zep[name] = {}
    zep[name]["num"] = 1
    zep[name]["cost"] = 0
    zep[name]["resources"] = {}
    for j in i.keys():
      if j != "name":
        zep[name]["resources"][j] = i[j]
    
    dc_into_name[(name,0)] = i["name"]
    name_into_dc[i["name"]] = (name,0)
    
  return (zep, dc_into_name, name_into_dc)  


def initialObjects(annotation):
  """
  Creates a new type of obj for every initially available obj
  It takes the annotation in json format.
  It returns the data to include in zephyrus input and the maps between the obj
  and its real name 
  """
  zep = {}
  obj_into_name = {}
  name_into_obj = {}
  
  for i in annotation["obj"]:
    name = settings.SEPARATOR + uuid.uuid4().hex
    zep[name] = {}
    for j in i.keys():
      if j != "name":
        zep[name]["provides"] = i["provides"]
        zep[name]["resources"] = { "initial_obj_resource" : 1}
    obj_into_name[name] = i["name"]
    name_into_obj[i["name"]] = name
  
  return (zep, obj_into_name, name_into_obj)


def extract_last_solution(inFile,outFile):
  """
  Extracts from a file the last solution saving it in another file.
  Rerturns true if a solutions is found.
  """
  solution = False
  sol = ""
  
  for line in reversed(open(inFile,'r').readlines()):
    if not solution:
      if line.startswith("----------"):
        solution = True
    else:
      if line.startswith("----------"):
        break
      else:
        sol = line + sol
  
  with open(outFile, 'w') as f:
    f.write(sol)
  return solution


def main(argv):
  """
  Main procedure extracting the JSON file from the ABS code,
  calls Zephyrus, and
  generates the ABS code
  """   
  output_file = ""
  
  try:
    opts, args = getopt.getopt(argv,"ho:vk",["help","ofile=","verbose","keep"])
  except getopt.GetoptError as err:
    print str(err)
    usage()
    sys.exit(1)
  for opt, arg in opts:
    if opt == '-h':
      usage()
      sys.exit()
    elif opt in ("-o", "--ofile"):
      output_file = arg
    elif opt in ("-k", "--keep"):
      global KEEP
      KEEP = True
    elif opt in ("-v", "--verbose"):
      log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
      log.info("Verbose output.")
  
  if len(args) != 1:
    print "1 argument is required"
    usage()
    sys.exit(1)
    
  input_file = args[0]   
  input_file = os.path.abspath(input_file)
  out_stream = sys.stdout
  if output_file:
    out_stream = open(output_file, "w") 

  global TMP_FILES  
  pid = str(os.getpgid(0))
  script_directory = os.path.dirname(os.path.realpath(__file__))
  
  log.info("Extracting JSON cost annotations from ABS code")
  annotation_file = "/tmp/" + pid + "_annotation.json"
  TMP_FILES = [ annotation_file ]
  proc = Popen( ["java", "-classpath", script_directory + "/absfrontend.jar",
        "autodeploy.Tester", "-JSON=" + annotation_file, input_file,
        script_directory + "/SmartDeployModule.abs"],
        cwd=script_directory, stdout=DEVNULL, stderr=DEVNULL )
  proc.wait()

  if not os.path.isfile(annotation_file): 
    log.critical("absfrontend execution terminated without writing its output file")
    log.critical("Exiting")
    sys.exit(1)

  log.info("Parsing JSON costs annotations file")
  annotation = remove_dots(read_json(annotation_file))
  log.debug("Internal json representation extracted from the abs program")
  log.debug(json.dumps(annotation, indent=1))
  
  log.info("Extracting class, resource, interface")
  class_names, resouce_names, interface_names = get_abs_names(annotation)
  
  log.debug("Classes")
  log.debug(class_names)
  log.debug("Resources")
  log.debug(resouce_names)
  log.debug("Interfaces")
  log.debug(interface_names)
  
  log.info("Extract smart deployment and dc annotations")
  try:
    (smart_dep_json, dc_json, module_name) = abs_extractor.get_annotation_from_abs(input_file)
  except ValueError:
    log.critical("Parsing error in JSON smart deployment annotations")
    log.critical("Exiting")
    sys.exit(1)
  
  log.debug("Smart deployment json annotation")
  log.debug(json.dumps(smart_dep_json, indent=1))
  log.debug("DC json annotation")
  log.debug(json.dumps(dc_json, indent=1))
  
  log.info("Printing common SmartDeployInterface interface and imports")
  code_generation.print_interface(module_name,interface_names,out_stream)
  
  log.info("Start generation of zephyrus json")
  
  initial_data = generate_zep_input_from_annotations(annotation)
  (interface_to_classes,class_to_interfaces) = code_generation.get_maps_interface_class(initial_data)
  
  log.info("Add location into zephyrus json")
  initial_data["locations"] = dc_json
  log.info("Add default location for deploying intial objects")
  initial_data["locations"].update(settings.DEFAULT_INITIAL_DC)
  
  for i in smart_dep_json:
    log.info("Processing " + i["id"])
    data = copy.deepcopy(initial_data)
    
    log.info("Adding new DC")
    newDC, dc_into_name, name_into_dc =  initialDC(i)
    data["locations"].update(newDC)
    
    log.info("Adding new obj")
    newObj, obj_into_name, name_into_obj =  initialObjects(i)
    data["components"].update(newObj)
    
    log.info("Parsing and adding specification")
    data["specification"] = decl_spec_lang.translate_specification(
                InputStream(i["specification"]),name_into_dc,name_into_obj)
    
    log.debug("Zephyrus input")
    log.debug(json.dumps(data,indent=1))    
    zephyrus_in_file = "/tmp/" + pid + i["id"] + "_zep_input.json"
    TMP_FILES.append(zephyrus_in_file)
    with open(zephyrus_in_file, 'w') as f:
      json.dump(data,f,indent=1)
         
    log.info("Running Zephyrus")
    zephyrus_out_file = "/tmp/" + pid + i["id"] + "_zep_output.txt"
    TMP_FILES.append(zephyrus_out_file)
    zephyrus2.zephyrus2.main(["-o",zephyrus_out_file,zephyrus_in_file])
    #zephyrus2.zephyrus2.main(["-v", "-o",zephyrus_out_file,zephyrus_in_file])
    
    log.info("Exctracting last solution")
    binding_in_file = "/tmp/" + pid + i["id"] + "_binding_in.json"
    TMP_FILES.append(binding_in_file)
    if not extract_last_solution(zephyrus_out_file,binding_in_file):
      log.info("No solution found for " + i["id"])
      continue
    else:
      log.debug("Zephyrus last solution")
      zep_last_conf = read_json(binding_in_file)
      log.debug(json.dumps(zep_last_conf,indent=1))
      
    log.info("Running bind optimizer")
    binding_out_file = "/tmp/" + pid + i["id"] + "_binding_out.json"
    TMP_FILES.append(binding_out_file)
    zephyrus2.bindings_optimizer.main(["-o",binding_out_file,zephyrus_in_file,binding_in_file])
    log.debug("Binding optimizer solution")
    bindings_opt_out = read_json(binding_out_file)
    log.debug(json.dumps(binding_out_file,indent=1))
    
    log.info("Generating ABS code")
    code_generation.print_class(i,interface_names,
      zep_last_conf, bindings_opt_out,
      annotation,
      dc_into_name, obj_into_name,
      out_stream)
  
  log.info("Print producline info")
  code_generation.print_productline(out_stream)    
  log.info("Clean.")
  clean()    
  log.info("Program Succesfully Ended")


if __name__ == "__main__":
  main(sys.argv[1:])