""" Module for translating the specification into binding preferences"""
__author__ = "Jacopo Mauro"
__copyright__ = "Copyright 2016, Jacopo Mauro"
__license__ = "ISC"
__version__ = "0.1"
__maintainer__ = "Jacopo Mauro"
__email__ = "mauro.jacopo@gmail.com"
__status__ = "Prototype"

from antlr4 import *
from antlr4 import InputStream
from bind_preference_grammar.BindPreferenceGrammarLexer import BindPreferenceGrammarLexer
from bind_preference_grammar.BindPreferenceGrammarParser import BindPreferenceGrammarParser
from bind_preference_grammar.BindPreferenceGrammarVisitor import BindPreferenceGrammarVisitor

import re
import settings
import uuid


class SpecificationParsingException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class MyVisitor(BindPreferenceGrammarVisitor):
    def __init__(self, name_into_DC, name_into_obj, class_names):
        """
    init some variables
    """
        BindPreferenceGrammarVisitor.__init__(self)
        self.name_into_DC = name_into_DC
        self.name_into_obj = name_into_obj
        self.class_names = class_names

    def defaultResult(self):
        return ""

    def visitTerminal(self, node):
        return node.getText()

    def aggregateResult(self, aggregate, nextResult):
        return aggregate + " " + nextResult

    def visitErrorNode(self, node):
        token = node.getSymbol()
        raise SpecificationParsingException("Erroneous Node at line " +
                                            str(token.line) + ", column " + str(token.column) + ": '" +
                                            str(token.text) + "'")

    def visitStatement(self, ctx):
        return ctx.getChild(0).accept(self)

    def visitAexprBind(self, ctx):
        prov = ctx.getChild(0).accept(self)
        req = ctx.getChild(3).accept(self)
        variable = "?x" + uuid.uuid4().hex
        return "(sum " + variable + " in ports : bind(" + prov + "," + req + ", " + variable + ")) > 0 "

    def visitAdcIDID(self, ctx):
        return ctx.getChild(0).accept(self) + '[0]'

    def visitAobjIDID(self, ctx):
        name = ctx.getChild(0).accept(self)
        if name in self.name_into_obj:
            return "'" + self.name_into_obj[name] + "'"
        assert(self.class_names[name])
        return "'" + self.class_names[name][0] + settings.SEPARATOR + name + "'"

    def visitAobjIDScenario(self, ctx):
        return "'" + ctx.getChild(2).accept(self) + settings.SEPARATOR + ctx.getChild(0).accept(self) + "'"

    def visitAobjIDRE(self, ctx):
        class_name = ctx.getChild(0).accept(self)
        pattern = ctx.getChild(2).accept(self).strip()[1:-1]
        matches = []
        for i in self.class_names[class_name]:
            if re.match(pattern, i):
                matches.append(i)
        if not matches:
            raise SpecificationParsingException("The regular expression " +
                                                   str(pattern) + " does not match with any scenario")
        s = "'[" + matches[0] + settings.SEPARATOR + class_name + "]"
        for i in matches[1:]:
            s += '|[' + i + settings.SEPARATOR + class_name + "]"
        return s + "'"

    def visitTypeV(self, ctx):
        txt = ctx.getChild(0).accept(self).strip()
        if txt == "DC":
            return "locations"
        else:
            return txt


def translate_preference(s,name_into_DC, name_into_obj, class_names):

    lexer = BindPreferenceGrammarLexer(InputStream(s))
    stream = CommonTokenStream(lexer)
    parser = BindPreferenceGrammarParser(stream)
    tree = parser.statement()
    visitor = MyVisitor(name_into_DC, name_into_obj, class_names)
    return visitor.visit(tree)
