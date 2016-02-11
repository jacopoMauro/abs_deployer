"""
Usage: abs_extractor <abs_program>
"""
from antlr4 import *
from ABSLexer import ABSLexer
from ABSParser import ABSParser
from ABSVisitor import ABSVisitor

import sys, getopt, os, json

class SpecificationParsingException(Exception):
  
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
    self.json = []
    
    
  def defaultResult(self):
    return ""
  
  
  def visitTerminal(self, node):
    return node.getText()
  
  
  def aggregateResult(self, aggregate, nextResult):
    return aggregate + "" + nextResult
  
  
  def visitErrorNode(self, node):
    raise SpecificationParsingException("Erroneous Node in parsing ABS")  
  
  
  def visitAnnotation(self, ctx):
    """
    Collects the annotations [ SmartDeploy : "..." ]
    """
    if ctx.getChildCount() == 5:
      name = ctx.getChild(1).accept(self)
      if name.endswith("SmartDeploy"):
        data = ctx.getChild(3).accept(self).decode("string-escape")[1:-1]
        self.json.append(json.loads(data))  
    return ""


def get_annotation_from_abs(abs_program_file):
  lexer = ABSLexer(FileStream(abs_program_file))
  stream = CommonTokenStream(lexer)
  parser = ABSParser(stream)
  tree = parser.goal()
  visitor = MyABSVisitor()
  visitor.visit(tree)
  return visitor.json
  

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