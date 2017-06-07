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
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.ErrorStrategy import DefaultErrorStrategy

import settings
import re

import sys, getopt, os


class DeclSpecLanguageParsingException(Exception):
  
  def __init__(self,value):
    self.value = value
  
  def __str__(self):
    return repr(self.value)


# class MyErrorListener( ErrorListener ):
# 
#     def __init__(self):
#         super(MyErrorListener, self).__init__()
# 
#     def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
#         raise DeclSpecLanguageParsingException("Parsing: syntax error!!")
# 
#     def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
#         raise DeclSpecLanguageParsingException("Ambiguity!!")
 
#     def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
#         raise DeclSpecLanguageParsingException("AttemptingFullContext")
# 
#     def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
#         raise DeclSpecLanguageParsingException("ContextSensitivity " + str(startIndex) + \
#             " " + str(stopIndex) + " " + str(prediction) + " " + str(configs))


# class MyErrorStrategy(DefaultErrorStrategy):
# 
#     def reportError(self, recognizer, e):
#         raise DeclSpecLanguageParsingException("Report Error")


class MyVisitor(DeclSpecLanguageVisitor):


  def __init__(self, name_into_DC, name_into_obj, class_names):
    """
    init some variables
    """    
    DeclSpecLanguageVisitor.__init__(self)
    self.name_into_DC = name_into_DC
    self.name_into_obj = name_into_obj
    self.class_names = class_names


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
  
  
  def visitStatement(self, ctx):
    return ctx.getChild(0).accept(self)
  
  
  def visitAtermId(self, ctx):
    obj = ctx.getChild(0).accept(self)
    ls = obj.split('||')
    s = ls[0]
    for i in ls[1:]: # in case of regexp matching more than one scenarios
      s += ' + ' + i
    return s
  
  
  def visitAtermDCObj(self, ctx):
    dc = ctx.getChild(0).accept(self)
    obj = ctx.getChild(2).accept(self)
    ls = obj.split('||')
    s = dc + '.' + ls[0]
    for i in ls[1:]: # in case of regexp matching more than one scenarios
      s += ' + ' + dc + '.' + i
    return s
  
  def visitAdcIDID(self, ctx):
    return ctx.getChild(0).accept(self) + '[0]'
  
  
  def visitAobjIDID(self, ctx):
    name = ctx.getChild(0).accept(self)
    assert self.class_names[name]
    scenario_name = self.class_names[name][0]
    return scenario_name + settings.SEPARATOR + name
  
  def visitAobjIDScenario(self, ctx):
    return ctx.getChild(2).accept(self) + settings.SEPARATOR + ctx.getChild(0).accept(self)
  
  
  def visitAobjIDRE(self, ctx):
    class_name = ctx.getChild(0).accept(self)
    pattern = ctx.getChild(2).accept(self).strip()[1:-1]
    matches = []
    for i in self.class_names[class_name]:
      if re.match(pattern, i):
        matches.append(i)
    if not matches:
      raise DeclSpecLanguageParsingException("The regular expression "  +
            str(pattern) + " does not match with any scenario")
    s = matches[0] + settings.SEPARATOR + class_name   
    for i in matches[1:]:
      s +=  '||' + i + settings.SEPARATOR + class_name
    return s
       
  
  
  def visitTypeV(self, ctx):
    txt = ctx.getChild(0).accept(self).strip()
    if txt == "DC":
      return "locations"
    elif txt == "obj":
      return "components"
    else:
      return txt
   

def translate_specification(file_stream, name_into_DC, name_into_obj,class_names):
  lexer = DeclSpecLanguageLexer(file_stream)
  stream = CommonTokenStream(lexer)
  parser = DeclSpecLanguageParser(stream)
#   parser._listeners = [ MyErrorListener() ]
#   parser._errHandler = BailErrorStrategy()
  tree = parser.statement()
  visitor = MyVisitor(name_into_DC, name_into_obj,class_names)
  spec = visitor.visit(tree)
#   initial obj installed only in one amount and in initial_DC  
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