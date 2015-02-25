from antlr4 import *
from SpecificationGrammarLexer import SpecificationGrammarLexer
from SpecificationGrammarParser import SpecificationGrammarParser
from SpecificationGrammarVisitor import SpecificationGrammarVisitor

import settings

class SpecificationParsingException(Exception):
  
  def __init__(self,value):
    self.value = value
  
  def __str__(self):
    return repr(self.value)

class MyVisitor(SpecificationGrammarVisitor):

  def __init__(self, classes, resources, interfaces ):
    """
    classes containing  a hash function mapping classes with scenarios
    resources and interfaces are simple hash functions containing
    the name of resources and interfaces
    """    
    SpecificationGrammarVisitor.__init__(self)
    self.classes = classes
    self.resources = resources
    self.interfaces = interfaces

  def defaultResult(self):
    return ""
  
  def visitTerminal(self, node):
    return node.getText()
  
  def aggregateResult(self, aggregate, nextResult):
    return aggregate + " " + nextResult
  
  def visitErrorNode(self, node):
    raise SpecificationParsingException("Erroneous Node")
    
  # Visit a parse tree produced by SpecificationGrammarParser#AexprNoDCInterface.
  def visitAexprNoDCInterface(self, ctx):
    interface_name = ctx.getChild(1).accept(self)
    if settings.INTERFACE_PREFIX + interface_name not in self.interfaces:
      raise SpecificationParsingException("Interface " + interface_name + " is not a valid interface name")
    return '#' + settings.INTERFACE_PREFIX + interface_name

  # Visit a parse tree produced by SpecificationGrammarParser#AexprNoDCClassScenario.
  def visitAexprNoDCClassScenario(self, ctx):
    class_name = ctx.getChild(1).accept(self)
    scenario_name = ctx.getChild(3).accept(self).upper()
    if class_name not in self.classes:
      raise SpecificationParsingException("Class " + class_name + " is not a valid class name")
    elif scenario_name not in self.classes[class_name]:
      raise SpecificationParsingException("Scenario " + scenario_name + " is not a valid scenario name ")
    return "#" + scenario_name + "___" + class_name + ":On"

  # Visit a parse tree produced by SpecificationGrammarParser#AexprNoDCClass.
  def visitAexprNoDCClass(self, ctx):
    class_name = ctx.getChild(1).accept(self)
    if class_name not in self.classes:
      raise SpecificationParsingException("Class " + class_name + " is not a valid class name")
    else:
      scenarios = self.classes[class_name]
      s = "#" + scenarios.pop() + settings.SEPARATOR + class_name + ":On"
      for i in scenarios:
        s += " + #" + i + settings.SEPARATOR + class_name + ":On"
    return s
    
  # Visit a parse tree produced by SpecificationGrammarParser#AresourceFilterOp.
  def visitAresourceFilterOp(self, ctx):
    resource_name = ctx.getChild(0).accept(self)
    if settings.RESOURCE_PREFIX + resource_name not in self.resources:
      raise SpecificationParsingException("Resource " + resource_name + " is not a valid resource name")
    return settings.RESOURCE_PREFIX + resource_name + " " + ctx.getChild(1).accept(self) + " " + ctx.getChild(2).accept(self)

  # Visit a parse tree produced by SpecificationGrammarParser#AexprDC.
  def visitAexprDC(self, ctx):
    res = ctx.getChild(1).accept(self)
    spec = ctx.getChild(3).accept(self)
    return "#(" + res + "){ _ : " + spec + "}"

  # Visit a parse tree produced by SpecificationGrammarParser#AexprDCNoFilter.
  def visitAexprDCNoFilter(self, ctx):
    spec = ctx.getChild(1).accept(self)
    return "#(_){ _ : " + spec + "}"
  

def translate_specification(inFile, classes, resources, interfaces):
  lexer = SpecificationGrammarLexer(FileStream(inFile))
  stream = CommonTokenStream(lexer)
  parser = SpecificationGrammarParser(stream)
  tree = parser.spec()
  visitor = MyVisitor(classes, resources, interfaces)
  return visitor.visit(tree)