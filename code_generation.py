'''
Procedures to generate the code code
'''

import toposort

def get_objects(conf):
  """
  Return the list of objects encoded in ( DC type, DC number, comp zeph name, comp number in DC )
  """
  ls = []
  for i in conf["locations"].keys():
    for j in conf["locations"][i].keys():
      for h in conf["locations"][i][j].kyes():
        for k in range(0,conf["locations"][i][j][h]):
          ls.append((i,int(j),h,k))
  return ls

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

