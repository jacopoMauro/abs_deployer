# Generated from DeclSpecLanguage.g4 by ANTLR 4.6
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by DeclSpecLanguageParser.

class DeclSpecLanguageVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DeclSpecLanguageParser#statement.
    def visitStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#b_expr.
    def visitB_expr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#b_term.
    def visitB_term(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#b_factor.
    def visitB_factor(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#relation.
    def visitRelation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#expr.
    def visitExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#AtermQuantifier.
    def visitAtermQuantifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#AtermInt.
    def visitAtermInt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#AtermId.
    def visitAtermId(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#AtermDCObj.
    def visitAtermDCObj(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#AtermSum.
    def visitAtermSum(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#AexprUnaryArithmetic.
    def visitAexprUnaryArithmetic(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#AtermBrackets.
    def visitAtermBrackets(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#typeV.
    def visitTypeV(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#AdcIDID.
    def visitAdcIDID(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#AdcIDVar.
    def visitAdcIDVar(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#AdcIDNum.
    def visitAdcIDNum(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#AobjIDID.
    def visitAobjIDID(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#AobjIDVar.
    def visitAobjIDVar(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#AobjIDScenario.
    def visitAobjIDScenario(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#AobjIDRE.
    def visitAobjIDRE(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#Avariable.
    def visitAvariable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#bool_binary_op.
    def visitBool_binary_op(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#arith_binary_op.
    def visitArith_binary_op(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#arith_unary_op.
    def visitArith_unary_op(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#comparison_op.
    def visitComparison_op(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#unaryOp.
    def visitUnaryOp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#boolFact.
    def visitBoolFact(self, ctx):
        return self.visitChildren(ctx)


