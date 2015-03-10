"""
Usage: abs_deployer.py [<options>] <abs program file> <target specification> <deployment components file>
  Options:
    -o, --ofile: file where to save the output
    -d, --dot: dot file where to save the configuration computed by Zephyrus
    -v, --verbose
"""

import json
import re
from subprocess import Popen
import sys, getopt
import os
import logging as log

import settings
import SpecificationGrammar.SpecTranslator as SpecTranslator

DEVNULL = open(os.devnull, 'wb')

#log.basicConfig(filename='example.log',level=log.DEBUG)
#log.basicConfig(level=log.DEBUG)

def usage():
  """Print usage"""
  print(__doc__)

def read_json(json_file): 
  json_data = open(json_file)
  data = json.load(json_data)
  json_data.close()
  return data

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


def generate_universe(data, universe_file):
  """Generate the universe file for Zephyrus and Metis"""

  universe = {
    "implementation" : {},
    "component_types" : [],
    "version" : 1, 
    "repositories" : [
      {
        "packages": [
          { "name": "mbs_stub_package" }
        ], 
        "name": "mbs"
      }]
    }
   
  for i in data["classes"]:

    component_name = i["name"]
        
    for j in i["activates"]:

      init_state = {
        "provide" : {},
        "require" : {},
        "initial" : True,
        "name" : "Init", 
        "successors" : ["On"] }
               
      state = {
        "provide" : {},
        "require" : {},
        "successors" : [],
        "name" : "On" }

      # handle provides
      provides = []
      if component_name in data["hierarchy"]:
        provides = data["hierarchy"][component_name]
        if len(provides) > 1:
          log.warning("Class implementing more than one interface not yet supported correctly")      
      for k in provides:
        state["provide"][settings.INTERFACE_PREFIX + k] =  j["provide"]
        
      # handles require ports
      requires = {}
      for k in j["sig"]:
        if k["type"] == "require" or k["type"] == "list":
          if k["value"] in requires:
            requires[k["value"]] += k["arity"]
          else:
            requires[k["value"]] = k["arity"]
      for k in requires.keys():
        state["require"][settings.INTERFACE_PREFIX + k] = requires[k]
            
      #name = component_name + SEPARATOR + j["scenario"] TEMPFIX
      if len(j["scenarios"]) > 1:
        log.critical("Multiple scenario feature is not supported")
        log.critical("Exiting")
        sys.exit(1)
      elif len(j["scenarios"]) == 0:
        name = settings.DEFAULT_SCENARIO_NAME + settings.SEPARATOR + component_name
      else:
        name = j["scenarios"][0].upper() + settings.SEPARATOR + component_name
      
      # for zephyrus specification resources should start with lowercase letter  
      costs = {}
      for k in j["cost"].keys():
        costs[settings.RESOURCE_PREFIX + k] = j["cost"][k]
        
      universe["component_types"].append({ "states" : [ init_state, state ], "name" : name, "consume" : costs})
      universe["implementation"][name] = [ { "repository": "mbs", "package": "mbs_stub_package" } ]
  
  with open(universe_file, 'w') as fo:
    json.dump(universe, fo, indent=1)       


def process_location_file(in_file, out_file, json_res):
  """Process the deployment component files generating the location file for Zephyrus.
  It changes the name of the resources and checks if the resources of abs are properly defined"""
    
  data = read_json(in_file)
  res = set([])
  
  counter = 0
  res_dict = {}
  res_cost = {}
  
  locs = { "version" : 1, "locations" : []}
  for i in data["DC_description"]:
    res_dict[i["name"]] = {}
    for j in i["provide_resources"].keys():
      res.add(settings.RESOURCE_PREFIX + j)
      res_dict[i["name"]][settings.RESOURCE_PREFIX + j] = i["provide_resources"][j]
      
    res_cost[i["name"]] = i["cost"]
       
  for i in data["DC_availability"].keys():
    if i not in res_dict:
      log.critical("Description of Deployment component " + i + " not found in the deployment component file")
      log.critical("Exiting")
      sys.exit(1)
    for j in range(int(data["DC_availability"][i])):
      locs["locations"].append({ "name" : i + settings.SEPARATOR +  str(counter),
                         "repository" : "mbs",
                         "provide_resources" : res_dict[i],
                         "cost" : res_cost[i] })
  
  log.debug("New location data")
  log.debug(locs)
  
  #check if resources given in the abs are present in the location file
  for i in json_res:
    if not i in res:
      log.critical("Resource " + i + "not found in the deployment component file")
      log.critical("Exiting")
      sys.exit(1)
      
  # write file
  with open(out_file, 'w') as fo:
    json.dump(locs, fo, indent=1) 
    
  return res
  


def plan_to_json(metis_output_file):
    """Extract from the Metis output the change state actions."""
    plans = []
    with open(metis_output_file, 'r') as f:
        for l in f:
            if re.match('.*change state.*', l):
                component_name = re.search('= \[(.*) :', l).group(1)
                #component_name = cn_to_armonic(component_name)
                state_from = re.search('from (.*) to', l).group(1)
                state_to = re.search('to (.*)]', l).group(1)
                plans.append({'component_name': component_name, 'state_from': state_from, 'state_to': state_to})
            else:
                pass
    return plans
  

def abs_id_rename(string):
  """Rename the string replacing dots and minus with underscores"""
  return "o" + string.replace(".","_").replace("-", "_")

def generate_abs_code(data, zephyrus, metis, dep_comp, output_stream):
  """Generate the ABS code from the Zephyrus and Metis outputs"""

  class_locations = {}
  class_bindings = {}
  class_types = {}
  signatures = {}
  used_locations = {}

  for i in zephyrus["components"]:
    class_locations[i["name"]] = i["location"]
    used_locations[i["location"]] = 0
    class_types[i["name"]] = i["type"].split(settings.SEPARATOR)[1]
    
  for i in zephyrus["bindings"]:
    if i["requirer"] not in class_bindings:
      class_bindings[i["requirer"]] = {}
    if i["port"] not in class_bindings[i["requirer"]]:
      class_bindings[i["requirer"]][i["port"]] = [ i["provider"] ]
    else:
      class_bindings[i["requirer"]][i["port"]].append(i["provider"])

  for i in data["classes"]:
    for j in i["activates"]:
      if len(j["scenarios"]) == 0:
        signatures[settings.DEFAULT_SCENARIO_NAME + settings.SEPARATOR + i["name"] ] = j["sig"]
      else:
        signatures[j["scenarios"][0].upper() + settings.SEPARATOR + i["name"] ] = j["sig"]
  
  output_stream.write("{\n")  
  for i in zephyrus["locations"]:
    if i["name"] in used_locations:
      output_stream.write("\tDeploymentComponent " + i["name"] +
                        " = new DeploymentComponent(\"" + i["name"] + "\", map[")
      name = i["name"].split(settings.SEPARATOR)[0]
      res = filter( lambda x: x["name"] == name, dep_comp["DC_description"])[0]["provide_resources"]
      resKeys = res.keys()
      while len(resKeys) > 0:
        j = resKeys.pop()
        output_stream.write("Pair(" + j + "," + str(res[j]) + ")")
        if len(resKeys) > 0:
          output_stream.write(", ")
      output_stream.write("]);\n") 
  
  for i in metis:
    name = i["component_name"]
    signature = signatures[name.split("-")[0]]
    output_stream.write("\t[DC: " + class_locations[name] + "] ")
    if len(data["hierarchy"][class_types[name]]) > 0:
      output_stream.write(data["hierarchy"][class_types[name]][0] +
                          " " + abs_id_rename(name) + " = ")
    output_stream.write( "new " + class_types[name] + "(")
    first_param = True
    for j in signature:
      if first_param:
        first_param = False
      else:
        output_stream.write(", ")
        
      if j["type"] == "require":
        output_stream.write(abs_id_rename(class_bindings[name][settings.INTERFACE_PREFIX + j["value"]].pop()))
      elif j["type"] == "user":
        output_stream.write(settings.SEPARATOR + j["value"] + settings.SEPARATOR)
      elif j["type"] == "default":
        output_stream.write(j["value"])
      elif j["type"] == "list":
        output_stream.write("list[")
        for _ in range(int(j["arity"])-1):
          output_stream.write(abs_id_rename(class_bindings[name][settings.INTERFACE_PREFIX + j["value"]].pop()) + ", ")
        output_stream.write(abs_id_rename(class_bindings[name][settings.INTERFACE_PREFIX + j["value"]].pop()) + "]")
      else:
        log.critical("The value " + j["value"] + " in signature not supported")
        log.critical("Exiting")
        sys.exit(1)
    output_stream.write(");\n")
  output_stream.write("}\n")


def main(argv):
  """Main procedure extracting the JSON file from the ABS code,
  generates the universe file, calls Zephyrus and Metis, and
  generates the ABS code"""   
  output_file = ""
  dot_file = ""
  
  try:
    opts, args = getopt.getopt(argv,"ho:vd:",["help","ofile=","verbose","dot="])
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
    elif opt in ("-d", "--dot"):
      dot_file = arg
    elif opt in ("-v", "--verbose"):
      log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
      log.info("Verbose output.")
  
  if len(args) != 3:
    print "3 arguments are required"
    usage()
    sys.exit(1)
    
  input_file = args[0]
  target = args[1]
  depl_file = args[2] 
  
  if input_file == "" or depl_file == "" or target == "":
    print "Input file not given. Please use -i, -d, -t options"
    usage()
    sys.exit(1)
  
  input_file = os.path.abspath(input_file)
  depl_file = os.path.abspath(depl_file)
  
  pid = str(os.getpgid(0))
  aeolus_universe = "/tmp/" + pid + "_universe.json"
  spec_file = "/tmp/" + pid + "_spec.spec"
  zephyrus_output = "/tmp/" + pid + "_zephyrus.json"
  metis_output = "/tmp/" + pid + "_metis.txt"
  absfrontend_file = "/tmp/" + pid + "_frontend.json"
  locations_file = "/tmp/" + pid + "_locations.json"

  log.info("Extracting JSON file from ABS code")
  script_directory = os.path.dirname(os.path.realpath(__file__))
  proc = Popen( ["java", "-classpath", script_directory + "/absfrontend.jar",
        "autodeploy.Tester", "-JSON=" + absfrontend_file, input_file],
        cwd=script_directory, stdout=DEVNULL )
  proc.wait()

  if proc.returncode != 0:
    log.critical("absfrontend execution terminated with return code " +  str(proc.returncode))
    log.critical("Exiting")
    sys.exit(1)
    
  log.info("Parsing JSON file")
  data = read_json(absfrontend_file)
  log.debug("Internal json representation")
  log.debug(json.dumps(data, indent=1))
  
  log.info("Extracting class, resource, interface")
  class_names, resouce_names, interface_names = get_abs_names(data)
  
  log.debug("Classes")
  log.debug(class_names)
  log.debug("Resources")
  log.debug(resouce_names)
  log.debug("Interfaces")
  log.debug(interface_names)
  
  log.info("Parsing location file")
  resouce_names = process_location_file(depl_file, locations_file,resouce_names)
  
  log.info("Generating universe file")
  generate_universe(data, aeolus_universe)
  
  log.info("Processing specification")
  try: 
    spec = SpecTranslator.translate_specification(target, class_names, resouce_names, interface_names)
  except SpecTranslator.SpecificationParsingException as e:
    log.critical("Parsing of the specification failed: " + e.value)
    log.critical("Exiting")
    sys.exit(1)
    
  log.debug("Zephyrus specification:")
  log.debug(spec)
  with open(spec_file, 'w') as f:
    f.write(spec) 
  
  log.debug("---UNIVERSE---")
  log.debug(json.dumps(read_json(aeolus_universe),indent=1))
  
  log.info("Running Zephyrus")
  if dot_file == "":
    proc = Popen( [settings.ZEPHYRUS_COMMAND, "-u", aeolus_universe, "-ic", locations_file,
         "-spec", spec_file, "-out", "stateful-json-v1", zephyrus_output,
         "-settings", script_directory + "/zephyrus.settings"],
         cwd=script_directory, stdout=DEVNULL )
  else:
    proc = Popen( [settings.ZEPHYRUS_COMMAND, "-u", aeolus_universe, "-ic", locations_file,
         "-spec", spec_file, "-out", "stateful-json-v1", zephyrus_output,
         "-out", "graph-deployment", dot_file,
         "-settings", script_directory + "/zephyrus.settings"],
         cwd=script_directory, stdout=DEVNULL )
  proc.wait()
  
  if proc.returncode == 14:
    log.critical("Zephyrus execution terminated with return code " +  str(proc.returncode))
    log.critical("Specification does not admit solutions")
    sys.exit(1)
  
  if proc.returncode != 0:
    log.critical("Zephyrus execution terminated with return code " +  str(proc.returncode))
    log.critical("It may be that there is no possible deployment solution.")
    log.critical("Exiting")
    sys.exit(1)

  log.debug("---FINAL CONFIGURATION---")
  log.debug(json.dumps(read_json(zephyrus_output),indent=1))
 
  log.info("Running Metis")
  proc = Popen( [settings.METIS_COMMAND, "-u", aeolus_universe, "-conf", zephyrus_output,
         "-o", metis_output], cwd=script_directory, stdout=DEVNULL )
  proc.wait()

  if proc.returncode != 0:
    log.critical("Metis execution terminated with return code " +  str(proc.returncode))
    log.critical("Exiting")
    sys.exit(1)

  
  log.debug("---FINAL PLAN---")
  log.debug(json.dumps(plan_to_json(metis_output),indent=1))

  log.info("Generating ABS Code")
  log.debug("---ABS Code---")
  
  if output_file == "":
    generate_abs_code(data, read_json(zephyrus_output), plan_to_json(metis_output), read_json(depl_file), sys.stdout)
  else:
    log.info("Writing to " + output_file)
    output_stream = open(output_file, 'w')
    generate_abs_code(data, read_json(zephyrus_output), plan_to_json(metis_output), read_json(depl_file), output_stream)
    output_stream.close()
      
  log.info("Removing temp files")
  os.remove(aeolus_universe)
  os.remove(zephyrus_output)
  os.remove(metis_output)
  os.remove(spec_file)
  os.remove(locations_file)
  log.info("Program Succesfully Ended")


if __name__ == "__main__":
  main(sys.argv[1:])