'''
code_generation.py: Procedures to generate the code code
'''
__author__ = "Jacopo Mauro"
__copyright__ = "Copyright 2016, Jacopo Mauro"
__license__ = "ISC"
__version__ = "0.1"
__maintainer__ = "Jacopo Mauro"
__email__ = "mauro.jacopo@gmail.com"
__status__ = "Prototype"

import toposort
import settings
import uuid
import logging as log
import sys


################################
# Auxiliary functions for the topsorting and fast data retrieval
################################

def get_map_obj_abs_name(zep_sol,initial_obj_into_name):
  """
  Return the list of objects encoded in ( DC type, DC number, comp zeph name, comp number in DC )
  """
  obj_to_abs_name = {}
  for i in zep_sol["locations"].keys():
    for j in zep_sol["locations"][i].keys():
      for h in zep_sol["locations"][i][j].keys():
        for k in range(0,zep_sol["locations"][i][j][h]):
          if h in initial_obj_into_name:
            obj_to_abs_name[(i,int(j),h,k)] = initial_obj_into_name[h]
          else:
            obj_to_abs_name[(i,int(j),h,k)] = (settings.OBJ_PREFIX + \
              h + "_" + str(k) + "_" + i + "_" + j).replace(".", "_")
  return obj_to_abs_name


def get_topological_sort(objs,bindings):
  """
  Performs the topological sort of the objects
  """  
  graph = {}
  for i in objs:
    graph[i] = set([])
  
  for i in bindings:
    graph[( i["req_location"],i["req_location_num"],i["req_comp"],i["req_comp_num"])].add(
      ( i["prov_location"],i["prov_location_num"],i["prov_comp"],i["prov_comp_num"]))
  
  return list(toposort.toposort(graph))


def get_maps_interface_class(zep_inp):
  """
  Takes the input of zephyrus and return the maps of
  interfaces to classes and viceversa
  """
  interface_to_classes = {}
  class_to_interfaces = {}
  for i in zep_inp["components"].keys():
    class_name = i.split(settings.SEPARATOR)[-1]
    interfaces = zep_inp["components"][i]["provides"][0]["ports"]
    class_to_interfaces[class_name] = interfaces
    for k in interfaces:
      if k in interface_to_classes:
        interface_to_classes[k].append(class_name)
      else:
        interface_to_classes[k] = [class_name]
  return (interface_to_classes,class_to_interfaces)


def get_map_dc_abs_names(zep_sol,initial_dc_into_name):
  """
  Takes the input the last solution of zephyrus and return the maps of
  dc to abs names
  """
  dc_to_abs_names = {}
  for i in zep_sol["locations"].keys():
    for j in zep_sol["locations"][i].keys():
      if (i,int(j)) in initial_dc_into_name.keys():
        dc_to_abs_names[(i,int(j))] = initial_dc_into_name[(i,int(j))]
      else:
        dc_to_abs_names[(i,int(j))] = i.replace(".","_") + "_" + j
  return dc_to_abs_names


def get_map_class_signature(cost_annotations):
  """
  Returns for every class its signature as defined in the cost annotations
  """
  class_to_signature = {}
  for i in cost_annotations["classes"]:
    class_name = i["name"]
    for j in i["activates"]:
      if j["scenarios"]:
        class_to_signature[(class_name,j["scenarios"][0])] = j["sig"]
      else:
        class_to_signature[(class_name,settings.DEFAULT_SCENARIO_NAME)] = j["sig"]
  return class_to_signature


def get_providers(bindings,(dcname,dcnum,objname,objnum)):
  prov = {}
  for i in bindings:
    if (dcname == i["req_location"] and
        dcnum == i["req_location_num"] and
        objname == i["req_comp"] and
        objnum == i["req_comp_num"]):


      obj = (i["prov_location"],i["prov_location_num"],i["prov_comp"],i["prov_comp_num"])
      if i["port"] in prov:
          prov[i["port"]].append(obj)
      else:
          prov[i["port"]] = [ obj ]
  return prov


################################
# Printing functions
################################


def print_class_signature(smart_dep_annotation,out):
  """
  Prints the first line of the class
  """
  out.write("class " + smart_dep_annotation["id"] + "(");
  out.write("CloudProvider cloudProvider")
  for i in smart_dep_annotation["DC"]:
    out.write(", DeploymentComponent " + i["name"])
  for i in smart_dep_annotation["obj"]:
    out.write(", " + i["interface"] + " " + i["name"])
  out.write(") implements SmartDeployInterface {\n")


def print_list_and_get_methods(interfaces,out):
  """
  Print the definition of the lists to store the DC and the objs
  """
  for i in interfaces:
    out.write("\tList<Pair<" + i + ",DeploymentComponent>> ls_" + i + " = Nil;\n")
  out.write("\tList<DeploymentComponent> ls_DeploymentComponent = Nil;\n")
  out.write("\n")    
  for i in interfaces:
    out.write("\tList<Pair<" + i + ",DeploymentComponent>> get" + i + "() { return ls_" + i + "; }\n")
  out.write("\tList<DeploymentComponent> getDeploymentComponent() ")
  out.write("{ return ls_DeploymentComponent; }\n")


def print_undeploy_method(interfaces,out):
  out.write("\tUnit undeploy() {\n")
  # to delete an object we delete its references
  for i in interfaces:
    out.write("\t\tls_" + i + " = Nil;\n")
  # we trigger the killInstance from the cloud provider
  out.write("\t\twhile ( !isEmpty(ls_DeploymentComponent) ) {\n")    
  out.write("\t\t\tcloudProvider.shutdownInstance(head(ls_DeploymentComponent));\n")
  out.write("\t\t\tls_DeploymentComponent = tail(ls_DeploymentComponent);\n")
  out.write("\t\t}\n")  
  out.write("\t}\n") 

def print_deploy_method(smart_dep_annotation, zep_last_conf,all_bindings,
      initial_dc_into_name, initial_obj_into_name,
      cost_annotations,
      out):
  out.write("\tUnit deploy() {\n")
  # start by deploying new DC
  dc_to_abs_names = get_map_dc_abs_names(zep_last_conf,initial_dc_into_name)
  for i in zep_last_conf["locations"].keys():
    # default DC and already existing DC do not need to be created 
    if not i.startswith(settings.SEPARATOR):
      for j in zep_last_conf["locations"][i].keys():
        out.write("\t\tDeploymentComponent " + dc_to_abs_names[(i,int(j))])
        out.write(" = cloudProvider.prelaunchInstanceNamed(\"" + i + "\");\n")
        out.write("\t\tls_DeploymentComponent = Cons(")
        out.write(dc_to_abs_names[(i,int(j))] + ",ls_DeploymentComponent);\n")
  # decide the order to create the obj and creating useful maps
  obj_to_abs_name = get_map_obj_abs_name(zep_last_conf,initial_obj_into_name)
  class_to_signature = get_map_class_signature(cost_annotations)

  # differentiate bindings that are optional and can be added later invoking a method from required bindings
  to_add_later_bindings = []
  bindings = []
  bindings_to_add_method = {}
  for i in all_bindings:
    scenario_name = i["req_comp"].split(settings.SEPARATOR)[0]
    class_name = i["req_comp"].split(settings.SEPARATOR)[-1]
    activates = [x["activates"] for x in cost_annotations["classes"] if x["name"] == class_name][0]
    if scenario_name == settings.DEFAULT_SCENARIO_NAME:
      opt_list_interfaces = activates[0]["optional_list"]
    else:
      opt_list_interfaces = [ x["optional_list"] for x in activates if x["scenarios"][0] == scenario_name ][0]
    if i["port"] in [x["interface"] for x in opt_list_interfaces]:
      to_add_later_bindings.append(i)
      bindings_to_add_method[(i["prov_comp"],i["req_comp"],i["port"])] = [y["method"] for y in opt_list_interfaces][0]
    else:
      bindings.append(i)

  # perform the topological sort
  try:
    installing_order = get_topological_sort(obj_to_abs_name.keys(),bindings)
  except ValueError:
    log.critical("Found a cycle in the final configuration. Impossible to proceed")
    log.critical("Exiting")
    sys.exit(1)

  for i in installing_order:
    for j in i:
      (dcname,dcnum,objname,_) = j
      if not objname.startswith(settings.SEPARATOR):
        scenario = objname.split(settings.SEPARATOR)[0]
        class_name = objname.split(settings.SEPARATOR)[-1]
        req_objects = get_providers(bindings,j)
        # printing the new construct
        out.write("\t\t[DC: " + dc_to_abs_names[(dcname,dcnum)] + "] ")
        out.write(cost_annotations["hierarchy"][class_name][0] + " ")
        out.write(obj_to_abs_name[j] + " = new ")
        out.write(class_name + "(")
        ls = []
        for k in class_to_signature[(class_name,scenario)]:
          if k["type"] == "require":
            ls.append(obj_to_abs_name[req_objects[k["value"]].pop()])
          elif k["type"] == "user":
            ls.append(settings.SEPARATOR + k["value"] + settings.SEPARATOR)
          elif k["type"] == "default":
            ls.append(k["value"])
          elif k["type"] == "list":
            arity = int(k["arity"])
            s = "list["
            if k["value"] in req_objects and req_objects[k["value"]]: # add in the list the remaining objects
            # fixme -> may give problems when the new requires later other objects of the same type
              s += obj_to_abs_name[req_objects[k["value"]].pop()]
              while req_objects[k["value"]]:
                s += ", " + obj_to_abs_name[req_objects[k["value"]].pop()]
            s += "]"
            ls.append(s)
        for k in range(len(ls)-1):
          out.write(ls[k] + ", ")
        if ls:
          out.write(ls[-1])
        out.write(");\n")
        # adding obj into the list
        interfaces = cost_annotations["hierarchy"][class_name]
        for k in interfaces:
          out.write("\t\tls_" + k + " = Cons(Pair(" + obj_to_abs_name[j] + "," + dc_to_abs_names[(dcname,dcnum)] + \
              "), ls_" + k + ");\n")
      else: # initial object with possible new incoming links
        for k in bindings:
          if objname == k["req_comp"] and (not k["prov_comp"].startswith(settings.SEPARATOR)): # if new object to add
            prov = (k["prov_location"], k["prov_location_num"], k["prov_comp"], k["prov_comp_num"])
            interface = k["port"]
            real_objname = obj_to_abs_name[j]
            for l in smart_dep_annotation["obj"]:
              if l["name"] == real_objname and "may_add_reference_to" in l:
                try:
                  method = next(x for x in l["may_add_reference_to"] if x["interface"] == interface)
                except StopIteration:
                  log.critical("The object " + real_objname + " requires a method to add " + obj_to_abs_name[prov])
                  log.critical("The method was not found")
                  log.critical("Exiting")
                  sys.exit(1)
            out.write("\t\t" + real_objname + "." + method["method"] + "(" + obj_to_abs_name[prov])
            if "DC_as_additional_parameter" in method and method["DC_as_additional_parameter"]:
                out.write("," + dc_to_abs_names[(k["prov_location"], k["prov_location_num"])])

            out.write(");\n" )

  # add the remaining optional bindings
  for i in to_add_later_bindings:
    prov = obj_to_abs_name[(i["prov_location"], i["prov_location_num"], i["prov_comp"], i["prov_comp_num"])]
    req = obj_to_abs_name[(i["req_location"], i["req_location_num"], i["req_comp"], i["req_comp_num"])]
    out.write("\t\t" + req + "." + bindings_to_add_method[(i["prov_comp"],i["req_comp"],i["port"])] + "(" + prov + ");\n")

  # ends deploy method
  out.write("\t}\n") 


def print_class(smart_dep_annotation,interfaces,
                zep_last_conf, bindings_opt_out,
                cost_annotations,
                initial_dc_into_name, initial_obj_into_name,
                out):
  """
  Prints the class implementing the SmartDeployInt interface
  """  
  out.write("adds ")
  print_class_signature(smart_dep_annotation,out)
  out.write("\n")
  print_list_and_get_methods(interfaces,out)
  out.write("\n")
  print_deploy_method(smart_dep_annotation,zep_last_conf, bindings_opt_out,
      initial_dc_into_name, initial_obj_into_name,
      cost_annotations, out)
  out.write("\n")
  print_undeploy_method(interfaces,out)
  out.write("}\n")


def print_interface(module_name,interfaces,out):
  """
  Prints the delta for modifying the SmartDeployInterface interface
  """
  
  out.write("module Delta" + uuid.uuid4().hex + ";\n")
  out.write("import * from ABS.DC;\n")
  out.write("import * from " + module_name + ";\n\n")
  out.write("delta SmartDeployDelta;\n")
  out.write("uses ABS.SmartDeploy;\n")  
  out.write("adds import * from " + module_name + ";\n")
  out.write("adds import * from ABS.DC;\n")
  out.write("modifies interface SmartDeployInterface {\n")
  for i in interfaces:
    out.write("\tadds List<Pair<" + i + ",DeploymentComponent>> get" + i + "();\n")
  out.write("\tadds List<DeploymentComponent> getDeploymentComponent();\n")
  out.write("\tadds Unit deploy();\n")
  out.write("\tadds Unit undeploy();\n")
  out.write("}\n")


def print_productline(out):
  out.write("\nproductline SmartDeployProductLine;\n")
  out.write("features SmartDeployFeature;\n")
  out.write("delta SmartDeployDelta when SmartDeployFeature;\n")
  out.write("product SmartDeploy (SmartDeployFeature);\n")