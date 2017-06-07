"""
abs_extractor.py:

Usage: abs_extractor <abs_program>
"""
__author__ = "Jacopo Mauro"
__copyright__ = "Copyright 2016, Jacopo Mauro"
__license__ = "ISC"
__version__ = "0.1"
__maintainer__ = "Jacopo Mauro"
__email__ = "mauro.jacopo@gmail.com"
__status__ = "Prototype"

from antlr4 import *
from ABSLexer import ABSLexer
from ABSParser import ABSParser
from ABSVisitor import ABSVisitor

import sys, getopt, os, json

import settings

# to allow the use of symmetry breaking constraints use a fictional resource
# associated to every different type of DC
fictional_resource_counter = 1

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
        self.deploy_annotations = []
        self.module_name = ""
        self.classes = {}
        self.interfaces = {}
  
    
    def defaultResult(self):
        return ""
  
  
    def visitTerminal(self, node):
        return node.getText()
  
  
    def aggregateResult(self, aggregate, nextResult):
        if isinstance(nextResult,list):
            return aggregate + str(nextResult)
        else:
            return aggregate + nextResult

  
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

    def visitClass_decl(self, ctx):
        # visit annotations
        if ctx.annotation():
            for i in ctx.annotation():
                i.accept(self)
        class_name = ctx.qualified_type_identifier().accept(self)
        interfaces = set()
        if ctx.interface_name():
            for i in ctx.interface_name():
                interfaces.add(i.accept(self))
        self.classes[class_name] = interfaces
        return ""

    def visitInterface_decl(self, ctx):
        # visit annotations
        if ctx.annotation():
            for i in ctx.annotation():
                i.accept(self)
        interface_name = ctx.qualified_type_identifier().accept(self)
        interfaces = set()
        if ctx.interface_name():
            for i in ctx.interface_name():
                interfaces.add(i.accept(self))
        self.interfaces[interface_name] = interfaces
        return ""


    def visitAnnotation(self, ctx):
        """
        Collects the annotations
        """
        def parse_json_string_in_annotation(s):
            s = s.strip().decode("string-escape")[1:-1]
            try:
              data = json.loads(s)
            except:
              raise ABSParsingException("Error in parsing the annotation " + s)
            return data

        if ctx.type_use():
            name = ctx.type_use().accept(self)
            if name == "SmartDeploy":
                self.smart_dep_json.append(parse_json_string_in_annotation(ctx.pure_exp().accept(self)))
            elif name == "SmartDeployCloudProvider":
                self.dc_json = parse_json_string_in_annotation(ctx.pure_exp().accept(self))
                fictional_resource_counter = 1
                for i in self.dc_json.keys():
                  self.dc_json[i]["num"] = settings.DEFAULT_NUMBER_OF_DC
                  if "cost" not in self.dc_json[i]:
                    self.dc_json[i]["cost"] = 0
                  self.dc_json[i]["resources"]['fictional_res'] = fictional_resource_counter
                  fictional_resource_counter += 1
            elif name == "Deploy":
                self.smart_dep_json.append(parse_json_string_in_annotation(ctx.pure_exp().accept(self)))
        return ""
  

def get_annotation_from_abs(abs_program_file):
    lexer = ABSLexer(FileStream(abs_program_file))
    stream = CommonTokenStream(lexer)
    parser = ABSParser(stream)
    tree = parser.goal()
    visitor = MyABSVisitor()
    visitor.visit(tree)
    return (
        visitor.smart_dep_json,
        visitor.dc_json,
        visitor.deploy_annotations,
        visitor.module_name,
        visitor.classes,
        visitor.interfaces
    )
  

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