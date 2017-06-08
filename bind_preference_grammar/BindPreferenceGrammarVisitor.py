# Generated from BindPreferenceGrammar.g4 by ANTLR 4.6
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by BindPreferenceGrammarParser.

class BindPreferenceGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BindPreferenceGrammarParser#statement.
    def visitStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#ApreferenceLocal.
    def visitApreferenceLocal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#ApreferenceExpr.
    def visitApreferenceExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#b_expr.
    def visitB_expr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#b_term.
    def visitB_term(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#b_factor.
    def visitB_factor(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#relation.
    def visitRelation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#expr.
    def visitExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#AexprQuantifier.
    def visitAexprQuantifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#AexprInt.
    def visitAexprInt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#AexprBind.
    def visitAexprBind(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#AexprSum.
    def visitAexprSum(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#AexprUnaryArithmetic.
    def visitAexprUnaryArithmetic(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#AexprBrackets.
    def visitAexprBrackets(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#AobjIDID.
    def visitAobjIDID(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#AobjIDVar.
    def visitAobjIDVar(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#AobjIDScenario.
    def visitAobjIDScenario(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#AobjIDRE.
    def visitAobjIDRE(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#typeV.
    def visitTypeV(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#bool_binary_op.
    def visitBool_binary_op(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#arith_binary_op.
    def visitArith_binary_op(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#arith_unary_op.
    def visitArith_unary_op(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#comparison_op.
    def visitComparison_op(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#unaryOp.
    def visitUnaryOp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#boolFact.
    def visitBoolFact(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#variable.
    def visitVariable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#re.
    def visitRe(self, ctx):
        return self.visitChildren(ctx)


