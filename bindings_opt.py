import json
import string
from subprocess import Popen
import sys, getopt
import os


def read_json(json_file): 
  json_data = open(json_file)
  data = json.load(json_data)
  json_data.close()
  return data


def generata_dzn(data, dzn_file):

  # map location with an int
  locations = {}

  # map components with their location
  components = {}

  prov_port_types = {}
  req_port_types = {}
  prov_port_locs = {}
  req_port_locs = {}

  port_types = {}
    
  location_num = 0
  for i in data["locations"]:
    locations[i["name"]] = location_num+1
    location_num += 1
    
  for i in data["components"]:
    components[i["name"]] = i["location"]
  
  binding_num = 0
  port_type_num = 0
  for i in data["bindings"]:
    if i["port"] not in port_types:
      port_types[i["port"]] = port_type_num+1
      port_type_num += 1  
      
    prov_port_types[binding_num] = port_types[i["port"]]
    prov_port_locs[binding_num] = locations[components[i["provider"]]]
    
    req_port_types[binding_num] = port_types[i["port"]]
    req_port_locs[binding_num] = locations[components[i["requirer"]]]
    
    binding_num += 1
    
  fo = open(dzn_file, "w")
    
  fo.write("locations = 1.." + str(location_num) + ";\n")
  fo.write("bindings = 1.." + str(binding_num) + ";\n")
  fo.write("types = 1.." + str(port_type_num) + ";\n")
  
  fo.write("prov_port_locations =")
  fo.write(str([ val for (key,val) in sorted(prov_port_locs.items())]))
  fo.write(";\n")
  
  fo.write("req_port_locations =")
  fo.write(str([ val for (key,val) in sorted(req_port_locs.items())]))
  fo.write(";\n")
  
  fo.write("prov_port_types =")
  fo.write(str([ val for (key,val) in sorted(prov_port_types.items())]))
  fo.write(";\n")
  
  fo.write("req_port_types =")
  fo.write(str([ val for (key,val) in sorted(req_port_types.items())]))
  fo.write(";\n")
  
  fo.close


def read_output(output_file):
  fo = open(output_file, "r")
  line = fo.readline().replace("\n","").split(" ")
  receivers = map( int, line) 
  fo.close()
  return receivers


def process_output(data,new_receivers):
  
  receivers = {}
  counter = 1
  for i in data["bindings"]:
    receivers[counter] = i["requirer"]
    counter += 1
  
  counter = 0
  for i in data["bindings"]:
    i["requirer"] = receivers[new_receivers[counter]]
    counter += 1

  return data

def main(argv):
   
  input_file = ""
  output_file = ""
  try:
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
  except getopt.GetoptError:
    print 'bindings_opt.py -i <inputfile> -o <outputfile>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'bindings_opt.py -i <inputfile> -o <outputfile>'
      sys.exit()
    elif opt in ("-i", "--ifile"):
      input_file = arg
    elif opt in ("-o", "--ofile"):
      output_file = arg

  if input_file == "" or output_file == "":
    print "Input or output file not specified. Please use both -i and -o options"
    sys.exit(2)
  
  input_file = os.path.abspath(input_file)
  output_file = os.path.abspath(output_file)
  
  pid = str(os.getpgid(0))
  dzn_file = "/tmp/" + pid + ".dzn"
  solution_file = "/tmp/" + pid + ".sol"
  best_solution_file = "/tmp/" + pid + ".best_solution"
  
  print "Parsing JSON file"
  data = read_json(input_file)
  print "Generating dzn file"
  generata_dzn(data, dzn_file)
  
  print "Running solver"
  script_directory = os.path.dirname(os.path.realpath(__file__))
  proc = Popen( ['minizinc', script_directory + "/bindings_opt.mzn", dzn_file, "-o", solution_file], cwd=script_directory)
  proc.wait()
  proc = Popen( ['solns2dzn', "-l", "-o", best_solution_file, solution_file])
  proc.wait()
  
  print "Process output"
  new_receivers = read_output(best_solution_file)
  data = process_output(data,new_receivers)
  
  print "Saving file"
  with open(output_file, 'w') as fo:
    json.dump(data, fo, indent=1)
  
  print "Removing temp files"
  os.remove(dzn_file)
  os.remove(solution_file)
  os.remove(best_solution_file)  
  print "Done :)"


if __name__ == "__main__":
   main(sys.argv[1:])