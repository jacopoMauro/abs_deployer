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

# global variable used to store the methods that needs to be called
# during the undeploy to remove references
to_remove_later_bindings = []

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


def get_map_class_signature(deploy_annotations):
  """
  Returns for every class its signature as defined in the cost annotations
  """
  class_to_signature = {}
  for i in deploy_annotations:
    class_name = i["class"]
    for j in i["scenarios"]:
      if j["name"]:
        class_to_signature[(class_name,j["name"])] = j["sig"]
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
  out.write(") implements " + smart_dep_annotation["id"] + "{\n")


def print_list_and_get_methods(interfaces,dc_json,out):
  """
  Print the definition of the lists to store the DC and the objs
  """
  for i in interfaces:
    out.write("\tList<List<" + i + ">> ls_ls_" + i + " = Nil;\n")
    out.write("\tList<" + i + "> ls_" + i + " = Nil;\n")
  out.write("\tList<List<DeploymentComponent>> ls_ls_DeploymentComponent = Nil;\n")
  out.write("\tList<DeploymentComponent> ls_DeploymentComponent = Nil;\n")
  print_cloud_provider_modification(dc_json, out)
  out.write("\n")    
  for i in interfaces:
    out.write("\tList<" + i + "> get" + i + "() { return ls_" + i + "; }\n")
  out.write("\tList<DeploymentComponent> getDeploymentComponent() { return ls_DeploymentComponent; }\n\n")

  out.write("\tUnit deploy() {\n")
  for i in interfaces:
    out.write("\t\tls_ls_" + i + " = Cons(ls_" + i + ",ls_ls_" + i + ");\n")
    out.write("\t\tls_" + i + " = Nil;\n")
  out.write("\t\tls_ls_DeploymentComponent = Cons(ls_DeploymentComponent,ls_ls_DeploymentComponent);\n")
  out.write("\t\tls_DeploymentComponent = Nil;\n")
  out.write("\t\tthis.deploy_aux();\n")
  out.write("\t}\n\n")


  out.write("\tUnit undeploy() {\n")
  out.write("\t\tif (ls_ls_DeploymentComponent != Nil) {\n")
  out.write("\t\t\tthis.undeploy_aux();\n")
  out.write("\t\t\tls_DeploymentComponent = head(ls_ls_DeploymentComponent);\n")
  out.write("\t\t\tls_ls_DeploymentComponent = tail(ls_ls_DeploymentComponent);\n")
  # out.write("\t\t\tif (ls_ls_DeploymentComponent != Nil) {\n")
  for i in interfaces:
    out.write("\t\t\t\tls_" + i + " = head(ls_ls_" + i + ");\n")
  # out.write("\t\t\t} else {\n")
  # for i in interfaces:
  #   out.write("\t\t\t\tls_" + i + " = Nil;\n")
  # out.write("\t\t\t}\n")
  for i in interfaces:
    # out.write("\t\tls_" + i + " = head(ls_ls_" + i + ");\n")
    out.write("\t\t\tls_ls_" + i + " = tail(ls_ls_" + i + ");\n")
  out.write("\t\t}\n")
  out.write("\t}\n\n")

def print_undeploy_method(smart_dep_annotation,interfaces,out):

  global to_remove_later_bindings

  out.write("\tUnit undeploy() {\n")




  out.write("\t}\n") 

def print_deploy_undeploy_method(smart_dep_annotation, zep_last_conf,all_bindings,
      initial_dc_into_name, initial_obj_into_name,
      deploy_annotations,classes_annotation,
      out):

  dep = "\tUnit deploy_aux() {\n"
  dep += "\t\tMap<DeploymentComponent,Rat> speedPatchMap = map[];\n"
  undep = "\tUnit undeploy_aux() {\n"

  # start by deploying new DC
  dc_to_abs_names = get_map_dc_abs_names(zep_last_conf,initial_dc_into_name)
  for i in zep_last_conf["locations"].keys():
    # default DC and already existing DC do not need to be created 
    if not i.startswith(settings.SEPARATOR):
      for j in zep_last_conf["locations"][i].keys():
        dep += "\t\tDeploymentComponent " + dc_to_abs_names[(i,int(j))]
        dep += " = cloudProvider.launchInstanceNamed(\"" + i + "\");\n"
        dep += "\t\tls_DeploymentComponent = Cons("
        dep += dc_to_abs_names[(i,int(j))] + ",ls_DeploymentComponent);\n"
############################################ runtime patch ###########################
        dep += "\t\tspeedPatchMap = put(speedPatchMap," + dc_to_abs_names[(i,int(j))] + ",0);\n"
######################################################################################
  # decide the order to create the obj and creating useful maps
  obj_to_abs_name = get_map_obj_abs_name(zep_last_conf,initial_obj_into_name)
  class_to_signature = get_map_class_signature(deploy_annotations)

  # differentiate bindings that are optional and can be added later invoking a method
  to_add_later_bindings = []
  to_remove_later_bindings = []
  bindings = []

  for i in all_bindings:
      if i["req_comp"] not in initial_obj_into_name.keys():
        scenario_name = i["req_comp"].split(settings.SEPARATOR)[0]
        class_name = i["req_comp"].split(settings.SEPARATOR)[-1]
        scenarios = [x["scenarios"] for x in deploy_annotations if x["class"] == class_name]
        assert(len(scenarios) == 1)
        methods = [x["methods"] for x in scenarios[0] if x["name"] == scenario_name]
        assert(len(methods) == 1)
        methods = methods[0]

        if i["port"] in [x["add"]["param_type"] for x in methods]:
          prov = obj_to_abs_name[(i["prov_location"], i["prov_location_num"], i["prov_comp"], i["prov_comp_num"])]
          req = obj_to_abs_name[(i["req_location"], i["req_location_num"], i["req_comp"], i["req_comp_num"])]
          add_rem = [y for y in methods if y["add"]["param_type"] == i["port"]][0]
          to_add_later_bindings.append((i["req_comp"].split(settings.SEPARATOR)[-1],
                                       add_rem["add"]["name"],
                                       "\t\t" + req + "." + add_rem["add"]["name"] + "(" + prov + ");\n"))
          if "remove" in add_rem:
            to_remove_later_bindings.append((i["req_comp"].split(settings.SEPARATOR)[-1],
                                             add_rem["remove"]["name"],
                                             "\t\t" + req + "." + add_rem["remove"]["name"] + "(" +
                                             (prov if "param_type" in add_rem["remove"] else "") + ");\n"))
        else:
          bindings.append(i)
      else: # initial object as a requirer
        bindings.append(i)

  # perform the topological sort
  try:
    installing_order = get_topological_sort(obj_to_abs_name.keys(),bindings)
  except ValueError:
    log.critical("Found a cycle in the final configuration. Impossible to proceed")
    log.critical("Exiting")
    sys.exit(1)

  counter = {} # counter of object per type inserted in type list
  for i in installing_order:
    for j in i:
      (dcname,dcnum,objname,_) = j
      if not objname.startswith(settings.SEPARATOR):
        scenario = objname.split(settings.SEPARATOR)[0]
        class_name = objname.split(settings.SEPARATOR)[-1]
        req_objects = get_providers(bindings,j)
        # printing the new construct for deployment
        dep += "\t\t[DC: " + dc_to_abs_names[(dcname,dcnum)] + "] "
        dep += classes_annotation[class_name][0] + " "
        dep += obj_to_abs_name[j] + " = new "
        dep += class_name + "("
        # print list of paramters for deployment
        ls = []
        for k in class_to_signature[(class_name,scenario)]:
          if k["kind"] == "require":
            ls.append(obj_to_abs_name[req_objects[k["type"]].pop()])
          # elif k["kind"] == "user":
          #   ls.append(settings.SEPARATOR + k["type"] + settings.SEPARATOR)
          elif k["kind"] == "constant":
            ls.append(k["value"])
          elif k["kind"] == "list":
            arity = int(k["num"])
            s = "list["
            if k["type"] in req_objects and req_objects[k["type"]]: # add in the list the remaining objects
            # fixme -> may give problems when the new requires later other objects of the same type
              s += obj_to_abs_name[req_objects[k["type"]].pop()]
              while req_objects[k["type"]]:
                s += ", " + obj_to_abs_name[req_objects[k["value"]].pop()]
            s += "]"
            ls.append(s)
        dep += ", ".join(ls) + ");\n"
        cores = [x["scenarios"][0]["cost"]["Cores"] for x in deploy_annotations if x["class"] == class_name]
        dep += "\t\tRat coreRequired_" + obj_to_abs_name[j] + " = " + str(cores[0]) + ";\n"
        dep += "\t\tspeedPatchMap = put(speedPatchMap, " + dc_to_abs_names[(dcname,dcnum)] + ", fromJust(lookup(speedPatchMap," + dc_to_abs_names[(dcname,dcnum)] + ")) + coreRequired_" + obj_to_abs_name[j] + ");\n"
        # adding obj into the list
        interfaces = classes_annotation[class_name]
        for k in interfaces:
          if k not in counter:
            counter[k] = 0
          else:
            counter[k] += 1
          dep += "\t\tls_" + k + " = Cons(" + obj_to_abs_name[j] + ", ls_" + k + ");\n"
          # only for the first interface
          if k == interfaces[0]:
            undep += "\t\t" + k + " " + obj_to_abs_name[j] + " = nth(ls_" + k + "," + unicode(counter[k]) + ");\n"
      else: # initial object with possible new incoming links (store what to print for later)
        for k in bindings:
          if objname == k["req_comp"] and (not k["prov_comp"].startswith(settings.SEPARATOR)): # if new object to add
            prov = (k["prov_location"], k["prov_location_num"], k["prov_comp"], k["prov_comp_num"])
            interface = k["port"]
            real_objname = obj_to_abs_name[j]
            for l in smart_dep_annotation["obj"]:
              if l["name"] == real_objname and "methods" in l and l["methods"]:
                method = [i for i in l["methods"] if i["add"]["param_type"] == interface ]
                assert len(method) == 1
                method = method[0]
            sdep = "\t\t" + real_objname + "." + method["add"]["name"] + "(" + obj_to_abs_name[prov] + ");\n"
            sundep = "\t\t" + real_objname + "." + method["remove"]["name"] + "("
            sundep += (obj_to_abs_name[prov] if "param_type" in method["remove"] else "") + ");\n"
            to_add_later_bindings.append((real_objname,
                                          method["add"]["name"],
                                          sdep))
            to_remove_later_bindings.append((real_objname,
                                             method["remove"]["name"],
                                             sundep))
  ####################### PATCH #######################
  dep += "\t\tthis!patchSpeed(speedPatchMap);\n"
  dep += "\t\tawait duration(waiting_time,waiting_time);\n"
  ######################################################
  # add the remaining optional bindings following the list priority
  if "add_method_priorities" in smart_dep_annotation:
        for i in smart_dep_annotation["add_method_priorities"]:
            for (class_name,method,s) in list(to_add_later_bindings):
                if i["class"] == class_name and i["method"] == method:
                    dep += s
                    to_add_later_bindings.remove((class_name,method,s))
  for (_,_,s) in to_add_later_bindings:
        dep += s

  # add the execution of methods to remove bindings added
  if "remove_method_priorities" in smart_dep_annotation:
        for i in smart_dep_annotation["remove_method_priorities"]:
            for (class_name,method,s) in list(to_remove_later_bindings):
                if i["class"] == class_name and i["method"] == method:
                    undep += s
                    to_remove_later_bindings.remove((class_name,method,s))
  for (_,_,s) in to_remove_later_bindings:
        undep += s

  # we trigger the killInstance from the cloud provider
  undep += "\t\twhile ( !isEmpty(ls_DeploymentComponent) ) {\n"
  undep +="\t\t\tcloudProvider.shutdownInstance(head(ls_DeploymentComponent));\n"
  undep +="\t\t\tls_DeploymentComponent = tail(ls_DeploymentComponent);\n"
  undep +="\t\t}\n"

  # ends
  dep += "\t}\n"
  undep += "\t}\n"

  out.write(dep)
  out.write("\n")
  out.write(undep)


def print_class(smart_dep_annotation,interfaces,
                zep_last_conf, bindings_opt_out,
                deploy_annotations, classes_annotation,
                initial_dc_into_name, initial_obj_into_name,
                module_name,dc_json,
                out):
  """
  Prints the class implementing the SmartDeployInt interface
  """
  print_module_and_interface(module_name,interfaces,smart_dep_annotation["id"],out)
  out.write("\n")
  print_class_signature(smart_dep_annotation,out)
  out.write("\n")
  print_list_and_get_methods(interfaces,dc_json,out)
  out.write("\n")
  print_deploy_undeploy_method(smart_dep_annotation,zep_last_conf, bindings_opt_out, initial_dc_into_name, initial_obj_into_name, deploy_annotations, classes_annotation,out)
  ######  runtime patch ########
  print_patch_speed(out)
  ############################
  out.write("}\n")

def print_cloud_provider_modification(dc_json, out):
  """
  Prints the class used to create the main deployer
  The name of this class is SmartDeployerCloudProviderImpl
  """
  ############# modified for time patching #############
  dcDescription = "\t{\n"
  max_time = 0
  for i in dc_json.keys():
    if "initial_DC" not in i:
      dcDescription += '\t\tcloudProvider.addInstanceDescription(Pair("' + unicode(i) + '",\n'
      dcDescription += '\t\t\tmap['
      dcDescription += 'Pair(CostPerInterval,' + unicode(dc_json[i]["cost"]) + ")\n"
      dcDescription += '\t\t\t,Pair(PaymentInterval,' + unicode(dc_json[i]["payment_interval"]) + ")\n"
      for j in dc_json[i]["resources"].keys():
  ######### find max startup duration ############
        if j == "Startupduration":
          time = int(unicode(dc_json[i]["resources"][j]))
          if time > max_time:
            max_time = time
##############can't specify startup duration into deployment components description it causes sequentialization of startup duration times#################################
        if j != "fictional_res" and j != "Startupduration":
          dcDescription += '\t\t\t,Pair(' + j + ',' + unicode(dc_json[i]["resources"][j]) + ")\n"
      dcDescription += '\t\t\t]));\n'
  out.write('\tRat waiting_time = ' + str(max_time) + ';\n') ####max waiting time
  out.write(dcDescription)
  out.write("\t}\n")

def print_module_and_interface(module_name,interfaces,name,out):
  """
  Prints the interface
  """
  out.write("module " + name + ";\n")
  out.write("export *;\n")
  out.write("import * from ABS.DC;\n")
  out.write("import * from " + module_name + ";\n\n")
  out.write("interface " + name + "{\n")
  for i in interfaces:
    out.write("\tList<" + i + "> get" + i + "();\n")
  out.write("\tList<DeploymentComponent> getDeploymentComponent();\n")
  out.write("\tUnit deploy();\n")
  out.write("\tUnit undeploy();\n")
  out.write("}\n")

################################  runtime patch  ############################################
def print_patch_speed(out):
  method = "\n\tUnit patchSpeed(Map<DeploymentComponent,Rat> dcs) {\n"
  method += "\t\tforeach(entry in entries(dcs)) {\n"
  method += "\t\t\tDeploymentComponent dc = fst(entry);\n"
  method += "\t\t\tRat coreUsed = snd(entry);\n"
  method += "\t\t\tInfRat speed_aux = await dc!total(Speed);\n"
  method += "\t\t\tRat total_speed = case speed_aux {\n"
  method += "\t\t\t\tFin(x) => x;\n"
  method += "\t\t\t\t_ => -1;\n"
  method += "\t\t\t};\n"
  method += "\t\t\tif(total_speed != -1) {\n"
  method += "\t\t\t\tRat totalCore = await dc!getNumberOfCores();\n"
  method += "\t\t\t\tRat speedPerCore = total_speed / totalCore;\n"
  method += "\t\t\t\tdc!decrementResources(total_speed - (speedPerCore * coreUsed), Speed);\n"
  method += "\t\t\t}\n"
  method += "\t\t}\n"
  method += "\t}\n"
  out.write(method)



