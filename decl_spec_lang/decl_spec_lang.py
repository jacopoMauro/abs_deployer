"""
decl_spec_lang.py:

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
from DeclSpecLanguageLexer import DeclSpecLanguageLexer
from DeclSpecLanguageParser import DeclSpecLanguageParser
from DeclSpecLanguageVisitor import DeclSpecLanguageVisitor

import settings

import sys, getopt, os

class DeclSpecLanguageParsingException(Exception):
  
  def __init__(self,value):
    self.value = value
  
  def __str__(self):
    return repr(self.value)

class MyVisitor(DeclSpecLanguageVisitor):


  def __init__(self, name_into_DC, name_into_obj):
    """
    init some variables
    """    
    DeclSpecLanguageVisitor.__init__(self)
    self.name_into_DC = name_into_DC
    self.name_into_obj = name_into_obj


  def defaultResult(self):
    return ""
  

  def visitTerminal(self, node):  
    txt = node.getText()
    if txt in self.name_into_DC:
      (name,val) = self.name_into_DC[txt]
      return name + "[" + str(val) + "]"
    elif txt in self.name_into_obj:
      return self.name_into_obj[txt]
    else:
      return txt
    

  def aggregateResult(self, aggregate, nextResult):
    return aggregate + " " + nextResult
  

  def visitErrorNode(self, node):
    token = node.getSymbol()    
    raise DeclSpecLanguageParsingException("Erroneous Node at line "  +
            str(token.line) + ", column " + str(token.column) + ": '" + 
            str(token.text) + "'"  )
  
  
  
  def visitAdcIDID(self, ctx):
    return ctx.getChild(0).accept(self) + '[0]'
  
  
  def visitAobjIDID(self, ctx):
    return settings.DEFAULT_SCENARIO_NAME + settings.SEPARATOR + ctx.getChild(0).accept(self)
  
  
  def visitAobjIDScenario(self, ctx):
    return ctx.getChild(2).accept(self) + settings.SEPARATOR + ctx.getChild(0).accept(self)
  
  
  def visitTypeV(self, ctx):
    txt = ctx.getChild(0).accept(self).strip()
    if txt == "DC":
      return "locations"
    elif txt == "obj":
      return "components"
    else:
      return txt
   

def translate_specification(file_stream, name_into_DC, name_into_obj):
  lexer = DeclSpecLanguageLexer(file_stream)
  stream = CommonTokenStream(lexer)
  parser = DeclSpecLanguageParser(stream)
  tree = parser.statement()
  visitor = MyVisitor(name_into_DC, name_into_obj)
  spec = visitor.visit(tree)
  # initial obj installed only in one amount and in initial_DC  
  for i in name_into_obj.values():
    spec += " and (" + i + " = 1)"
    spec += " and (" + settings.DEFAULT_INITIAL_DC.keys()[0] + "[0]." + i + "= 1)"
  # add preference: minimize cost and then number of components
  spec += "; cost; sum ?x in locations : (sum ?y in components: ?x.?y)"
  return spec


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
  print translate_specification(FileStream(input_file), {}, {})

  
if __name__ == "__main__":
  main(sys.argv[1:])