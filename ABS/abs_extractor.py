"""
Usage: abs_extractor <abs_program>
"""
from antlr4 import *
from ABSLexer import ABSLexer
from ABSParser import ABSParser
from ABSVisitor import ABSVisitor

import sys, getopt, os, json

import settings

class ABSParsingException(Exception):
  
  def __init__(self,value):
    self.value = value
  
  def __str__(self):
    return repr(self.value)
  
  
class MyABSVisitor(ABSVisitor):
  
  
  def __init__(self):
    """
    classes to extract the annotations and smart deploy instances form the 
    abs program
    """    
    ABSVisitor.__init__(self)
    self.smart_dep_json = []
    self.dc_json = {}
    self.module_name = ""
  
    
  def defaultResult(self):
    return ""
  
  
  def visitTerminal(self, node):
    return node.getText()
  
  
  def aggregateResult(self, aggregate, nextResult):
    if isinstance(nextResult,list):
      return aggregate + " " +  str(nextResult)
    else:
      return aggregate + " " + nextResult

  
  def visitErrorNode(self, node):
    token = node.getSymbol()    
    raise ABSParsingException("Erroneous Node at line "  +
            str(token.line) + ", column " + str(token.column) + ": '" + 
            str(token.text) + "'"  )
  
  
  def visitModule_decl(self, ctx):
    self.module_name = ctx.getChild(1).accept(self).strip()
    for i in range(3,ctx.getChildCount()):
      ctx.getChild(i).accept(self)
    return ""
  
  
  def visitAnnotation(self, ctx):
    """
    Collects the annotations [ SmartDeploy : "..." ]
    """
    if ctx.getChildCount() == 5:
      name = ctx.getChild(1).accept(self).strip()
      if name == "SmartDeploy":
        data = ctx.getChild(3).accept(self).strip().decode("string-escape")[1:-1]
        self.smart_dep_json.append(json.loads(data))  
    return ""
  
  
  def visitSyncCallExp(self, ctx):
    """
    Try to find synccall with name setInstanceDescriptions to get the DC
    specification.
    """
    if ctx.getChild(2).accept(self).strip() == "setInstanceDescriptions":
      cloud_name = ctx.getChild(0).accept(self).strip()
      params = ctx.getChild(4).accept(self)[0]
      try:
        data = json.loads(params)
      except ValueError:
        raise ABSParsingException("CloudProvider parsing failed")
      
      # example JSON from parser
      # [{"c3.xlarge": [{"CostPerInterval": 210},{"Memory": 750}]}]
      # transformed into JSON for Zephyrus "locations" : XXX
      for i in data:
        for j in i.keys():
          self.dc_json[j] = {
                  "num": settings.DEFAULT_NUMBER_OF_DC,
                  "resources": {},
                  "cost":0 }
          for k in i[j]:
            for h in k.keys():
              if h == "CostPerInterval":
                self.dc_json[j]["cost"] = k[h]
              else:
                self.dc_json[j]["resources"][h] = k[h]
    return ""
  
  
  def visitConstructorExp(self, ctx):
    """
    Dicriminate Pair and Map Constructors to transform an ABS string into a
    JSON like string.
    """
    qualifier = ctx.getChild(0).accept(self).strip()
    if qualifier == "Pair":
      ls = ctx.getChild(2).accept(self)
      return "{" + ls[0] + ": " + ls[1] + "}"
    elif qualifier == "InsertAssoc":
      ls = ctx.getChild(2).accept(self)
      if ls[1] == '"EmptyMap"':
        return  "["  + ls[0] + "]"
      else:
        return "[" + ls[0] + "," + ls[1][1:]
    else:
      return '"' + qualifier +'"'
  
  
  def visitPure_exp_list(self, ctx):
    """
    Pure expression lists return a list, not a string.
    """
    n = ctx.getChildCount()
    ls = []
    for i in range(0,n,2):
      ls.append(ctx.getChild(i).accept(self).strip())
    return ls


def get_annotation_from_abs(abs_program_file):
  lexer = ABSLexer(FileStream(abs_program_file))
  stream = CommonTokenStream(lexer)
  parser = ABSParser(stream)
  tree = parser.goal()
  visitor = MyABSVisitor()
  visitor.visit(tree)
  return (visitor.smart_dep_json, visitor.dc_json, visitor.module_name)
  

def main(argv):
   
  try:
    opts, args = getopt.getopt(argv,"",[])
  except getopt.GetoptError as err:
    print str(err)
    print(__doc__)
    sys.exit(1)
  
  if len(args) != 1:
    print "1 argument is required"
    print(__doc__)
    sys.exit(1)
    
  input_file = args[0]   
  input_file = os.path.abspath(input_file) 
  print json.dumps(get_annotation_from_abs(input_file), indent=1)

  
if __name__ == "__main__":
  main(sys.argv[1:])