"""
Usage: abs_deployer.py [<options>] <abs program file>
  Options:
    -o, --ofile: file where to save the output
    -v, --verbose
    -k, --keep: keep temp files
"""

import json
import uuid
import re
from subprocess import Popen
import sys, getopt
import os
import logging as log
import signal
import psutil

import settings
import SpecificationGrammar.SpecTranslator as SpecTranslator
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
        classes[i["name"]].append(j["scenarios"][0].upper())
      
      for k in j["cost"].keys():
        resources.add(settings.RESOURCE_PREFIX + k)
  
  for i in data["hierarchy"]:
    for j in data["hierarchy"][i]:
      interfaces.add(settings.INTERFACE_PREFIX + j)
    
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
        name = j["scenarios"][0].upper() + settings.SEPARATOR + component_name
      
      zep["components"][name] = comp
  return zep


# def generate_abs_code(data, zephyrus, metis, dep_comp, output_stream):
#   """Generate the ABS code from the Zephyrus and Metis outputs"""
# 
#   class_locations = {}
#   class_bindings = {}
#   class_types = {}
#   signatures = {}
#   used_locations = {}
# 
#   for i in zephyrus["components"]:
#     class_locations[i["name"]] = i["location"]
#     used_locations[i["location"]] = 0
#     class_types[i["name"]] = i["type"].split(settings.SEPARATOR)[1]
#     
#   for i in zephyrus["bindings"]:
#     if i["requirer"] not in class_bindings:
#       class_bindings[i["requirer"]] = {}
#     if i["port"] not in class_bindings[i["requirer"]]:
#       class_bindings[i["requirer"]][i["port"]] = [ i["provider"] ]
#     else:
#       class_bindings[i["requirer"]][i["port"]].append(i["provider"])
# 
#   for i in data["classes"]:
#     for j in i["activates"]:
#       if len(j["scenarios"]) == 0:
#         signatures[settings.DEFAULT_SCENARIO_NAME + settings.SEPARATOR + i["name"] ] = j["sig"]
#       else:
#         signatures[j["scenarios"][0].upper() + settings.SEPARATOR + i["name"] ] = j["sig"]
#   
#   output_stream.write("{\n")  
#   for i in zephyrus["locations"]:
#     if i["name"] in used_locations:
#       output_stream.write("\tDeploymentComponent " + i["name"] +
#                         " = new DeploymentComponent(\"" + i["name"] + "\", map[")
#       name = i["name"].split(settings.SEPARATOR)[0]
#       res = filter( lambda x: x["name"] == name, dep_comp["DC_description"])[0]["provide_resources"]
#       resKeys = res.keys()
#       while len(resKeys) > 0:
#         j = resKeys.pop()
#         # for ABS only CPU, Memory, and Bandwidth can be used
#         if j == "CPU" or j == "Memory" or j == "Bandwidth":
#           output_stream.write("Pair(" + j + "," + str(res[j]) + ")")
#           if len(resKeys) > 0:
#             output_stream.write(", ")
#       output_stream.write("]);\n") 
#   
#   for i in metis:
#     name = i["component_name"]
#     signature = signatures[name.split("-")[0]]
#     output_stream.write("\t[DC: " + class_locations[name] + "] ")
#     if len(data["hierarchy"][class_types[name]]) > 0:
#       output_stream.write(data["hierarchy"][class_types[name]][0] +
#                           " " + abs_id_rename(name) + " = ")
#     output_stream.write( "new " + class_types[name] + "(")
#     first_param = True
#     for j in signature:
#       if first_param:
#         first_param = False
#       else:
#         output_stream.write(", ")
#         
#       if j["type"] == "require":
#         output_stream.write(abs_id_rename(class_bindings[name][settings.INTERFACE_PREFIX + j["value"]].pop()))
#       elif j["type"] == "user":
#         output_stream.write(settings.SEPARATOR + j["value"] + settings.SEPARATOR)
#       elif j["type"] == "default":
#         output_stream.write(j["value"])
#       elif j["type"] == "list":
#         output_stream.write("list[")
#         for _ in range(int(j["arity"])-1):
#           output_stream.write(abs_id_rename(class_bindings[name][settings.INTERFACE_PREFIX + j["value"]].pop()) + ", ")
#         output_stream.write(abs_id_rename(class_bindings[name][settings.INTERFACE_PREFIX + j["value"]].pop()) + "]")
#       else:
#         log.critical("The value " + j["value"] + " in signature not supported")
#         log.critical("Exiting")
#         sys.exit(1)
#     output_stream.write(");\n")
#   output_stream.write("}\n")


def initialDC(annotation):
  """
  Creates a new type of DC for every initially available DC
  It takes the annotation in json format.
  It returns the data to include in zephyrus input and the maps between the DC
  components and its real name 
  """
  zep = {}
  DC_into_names = {}
  names_into_DC = {}
  
  for i in annotation["DC"]:
    name = uuid.uuid4().hex
    zep[name] = {}
    zep[name]["num"] = 1
    zep[name]["cost"] = 0
    zep[name]["resources"] = {}
    for j in i.keys():
      if j != "name":
        zep[name]["resources"][j] = i[j]
    
    DC_into_names[(name,0)] = i["name"]
    names_into_DC[i["name"]] = (name,0)
  
  return (zep, DC_into_names, names_into_DC)  


def initialObjects(annotation):
  """
  Creates a new type of obj for every initially available obj
  It takes the annotation in json format.
  It returns the data to include in zephyrus input and the maps between the obj
  and its real name 
  """
  zep = {}
  obj_into_names = {}
  names_into_obj = {}
  
  for i in annotation["obj"]:
    name = uuid.uuid4().hex
    zep[name] = {}
    for j in i.keys():
      if j != "name":
        zep[name]["provides"] = i["provides"]
        zep[name]["resources"] = {} # no resource consumption
  obj_into_names[name] = i["name"]
  names_into_obj[i["name"]] = name
  
  return (zep, obj_into_names, names_into_obj)


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
  global TMP_FILES  
  pid = str(os.getpgid(0))
  script_directory = os.path.dirname(os.path.realpath(__file__))
  
  log.info("Extracting JSON cost annotations from ABS code")
  annotation_file = "/tmp/" + pid + "_annotation.json"
  TMP_FILES = [ annotation_file ]
  proc = Popen( ["java", "-classpath", script_directory + "/absfrontend.jar",
        "autodeploy.Tester", "-JSON=" + annotation_file, input_file],
        cwd=script_directory, stdout=DEVNULL )
  proc.wait()

  if proc.returncode != 0:
    # TODO check if output file exists
    log.critical("absfrontend execution terminated with return code " +  str(proc.returncode))
    log.critical("Exiting")
    sys.exit(1)

  log.info("Parsing JSON costs annotations file")
  annotation = remove_dots(read_json(annotation_file))
  log.debug("Internal json representation extracted from teh abs program")
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
    (smart_dep_json, dc_json) = abs_extractor.get_annotation_from_abs(input_file)
  except ValueError:
    log.critical("Parsing error in JSON smart deployment annotations")
    log.critical("Exiting")
    sys.exit(1)
  
  log.debug("Smart deployment json annotation")
  log.debug(json.dumps(smart_dep_json, indent=1))
  log.debug("DC json annotation")
  log.debug(json.dumps(dc_json, indent=1))
  
  log.info("Start generation of zephyrus json")
  initial_data = generate_zep_input_from_annotations(annotation)
  
  log.info("Add location into zephyrus json")
  initial_data["locations"] = dc_json
 
  for i in smart_dep_json:
    log.info("Processing " + i["id"])
    data = dict(initial_data)
    log.info("Adding new DC")
    newDC, DC_into_names, names_into_DC =  initialDC(i)
    data["locations"].update(newDC)
    
    log.info("Adding new obj")
    newObj, obj_into_names, names_into_obj =  initialObjects(i)
    
    log.debug("Zephyrus input")
    log.debug(json.dumps(data,indent=1))
    
    log.info("Parsing specification")
    # TODO
    # add initial obj constraints in the specification
    spec = i["specification"]
    log.debug("Specfication")
    log.debug(spec)
 
  
  
  
  
#   resouce_names = process_location_file(depl_file, locations_file,resouce_names)
#   
#   log.info("Generating universe file")
#   generate_universe(data, aeolus_universe)
#   
#   log.info("Processing specification")
#   try: 
#     spec = SpecTranslator.translate_specification(target, class_names, resouce_names, interface_names)
#   except SpecTranslator.SpecificationParsingException as e:
#     log.critical("Parsing of the specification failed: " + e.value)
#     log.critical("Exiting")
#     sys.exit(1)
#     
#   log.debug("Zephyrus specification:")
#   
#   with open(spec_file, 'w') as f:
#     f.write(spec) 
#   
#   log.debug("---UNIVERSE---")
#   log.debug(json.dumps(read_json(aeolus_universe),indent=1))
#   
#   log.info("Running Zephyrus")
#   if dot_file == "":
#     proc = Popen( [settings.ZEPHYRUS_COMMAND, "-u", aeolus_universe, "-ic", locations_file,
#          "-spec", spec_file, "-out", "stateful-json-v1", zephyrus_output,
#          "-settings", script_directory + "/zephyrus.settings"],
#          cwd=script_directory, stdout=DEVNULL )
#   else:
#     proc = Popen( [settings.ZEPHYRUS_COMMAND, "-u", aeolus_universe, "-ic", locations_file,
#          "-spec", spec_file, "-out", "stateful-json-v1", zephyrus_output,
#          "-out", "graph-deployment", dot_file,
#          "-settings", script_directory + "/zephyrus.settings"],
#          cwd=script_directory, stdout=DEVNULL )
#   proc.wait()
#   
#   if proc.returncode == 14:
#     log.critical("Zephyrus execution terminated with return code " +  str(proc.returncode))
#     log.critical("Specification does not admit solutions")
#     sys.exit(1)
#   
#   if proc.returncode != 0:
#     log.critical("Zephyrus execution terminated with return code " +  str(proc.returncode))
#     log.critical("Exiting")
#     sys.exit(1)
# 
#   log.debug("---FINAL CONFIGURATION---")
#   log.debug(json.dumps(read_json(zephyrus_output),indent=1))
#   
#   log.debug("---RUN BINDINGS OPTIMIZER---")
#   proc = Popen( ["python", "bindings_opt.py", "-i", zephyrus_output,
#                   "-o", zephyrus_output_opt], cwd=script_directory, stdout=DEVNULL )
#   proc.wait()
#   
#   if proc.returncode != 0:
#     log.critical("Bindings optimizer terminated with return code " +  str(proc.returncode))
#     log.critical("Exiting")
#     sys.exit(1)
#   log.debug(json.dumps(read_json(zephyrus_output_opt),indent=1))
#  
#   log.info("Running Metis")
#   proc = Popen( [settings.METIS_COMMAND, "-u", aeolus_universe, "-conf", zephyrus_output_opt,
#          "-o", metis_output], cwd=script_directory, stdout=DEVNULL )
#   proc.wait()
# 
#   if proc.returncode != 0:
#     log.critical("Metis execution terminated with return code " +  str(proc.returncode))
#     log.critical("Exiting")
#     sys.exit(1)
# 
#   
#   log.debug("---FINAL PLAN---")
#   log.debug(json.dumps(plan_to_json(metis_output),indent=1))
# 
#   log.info("Generating ABS Code")
#   log.debug("---ABS Code---")
#   
#   if output_file == "":
#     generate_abs_code(data, read_json(zephyrus_output_opt), plan_to_json(metis_output), read_json(depl_file), sys.stdout)
#   else:
#     log.info("Writing to " + output_file)
#     output_stream = open(output_file, 'w')
#     generate_abs_code(data, read_json(zephyrus_output_opt), plan_to_json(metis_output), read_json(depl_file), output_stream)
#     output_stream.close()
      
  log.info("Clean.")
  clean()    
  log.info("Program Succesfully Ended")


if __name__ == "__main__":
  main(sys.argv[1:])