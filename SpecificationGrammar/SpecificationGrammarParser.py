# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .SpecificationGrammarVisitor import SpecificationGrammarVisitor
else:
    from SpecificationGrammarVisitor import SpecificationGrammarVisitor

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\33\u0083\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3")
        buf.write(u"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2$\n\2\3\2\3")
        buf.write(u"\2\3\2\3\2\7\2*\n\2\f\2\16\2-\13\2\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3;\n\3\3\3\3\3\3\3\3")
        buf.write(u"\3\7\3A\n\3\f\3\16\3D\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write(u"\4\3\4\7\4N\n\4\f\4\16\4Q\13\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write(u"\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5`\n\5\3\5\3\5\3\5\3")
        buf.write(u"\5\7\5f\n\5\f\5\16\5i\13\5\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write(u"\6\3\6\3\6\3\6\3\6\3\6\5\6w\n\6\3\7\3\7\3\b\3\b\3\t\3")
        buf.write(u"\t\3\n\3\n\3\13\3\13\3\13\2\6\2\4\6\b\f\2\4\6\b\n\f\16")
        buf.write(u"\20\22\24\2\5\3\2\20\25\3\2\26\30\3\2\13\f\u0087\2#\3")
        buf.write(u"\2\2\2\4:\3\2\2\2\6E\3\2\2\2\b_\3\2\2\2\nv\3\2\2\2\f")
        buf.write(u"x\3\2\2\2\16z\3\2\2\2\20|\3\2\2\2\22~\3\2\2\2\24\u0080")
        buf.write(u"\3\2\2\2\26\27\b\2\1\2\27\30\5\22\n\2\30\31\5\2\2\6\31")
        buf.write(u"$\3\2\2\2\32\33\7\3\2\2\33\34\5\2\2\2\34\35\7\4\2\2\35")
        buf.write(u"$\3\2\2\2\36$\5\24\13\2\37 \5\4\3\2 !\5\f\7\2!\"\5\4")
        buf.write(u"\3\2\"$\3\2\2\2#\26\3\2\2\2#\32\3\2\2\2#\36\3\2\2\2#")
        buf.write(u"\37\3\2\2\2$+\3\2\2\2%&\f\7\2\2&\'\5\20\t\2\'(\5\2\2")
        buf.write(u"\b(*\3\2\2\2)%\3\2\2\2*-\3\2\2\2+)\3\2\2\2+,\3\2\2\2")
        buf.write(u",\3\3\2\2\2-+\3\2\2\2./\b\3\1\2/\60\7\5\2\2\60\61\5\6")
        buf.write(u"\4\2\61\62\7\6\2\2\62\63\5\b\5\2\63\64\7\7\2\2\64;\3")
        buf.write(u"\2\2\2\65\66\7\5\2\2\66\67\5\b\5\2\678\7\7\2\28;\3\2")
        buf.write(u"\2\29;\5\n\6\2:.\3\2\2\2:\65\3\2\2\2:9\3\2\2\2;B\3\2")
        buf.write(u"\2\2<=\f\4\2\2=>\5\16\b\2>?\5\4\3\5?A\3\2\2\2@<\3\2\2")
        buf.write(u"\2AD\3\2\2\2B@\3\2\2\2BC\3\2\2\2C\5\3\2\2\2DB\3\2\2\2")
        buf.write(u"EF\b\4\1\2FG\7\31\2\2GH\5\f\7\2HI\7\32\2\2IO\3\2\2\2")
        buf.write(u"JK\f\3\2\2KL\7\b\2\2LN\5\6\4\4MJ\3\2\2\2NQ\3\2\2\2OM")
        buf.write(u"\3\2\2\2OP\3\2\2\2P\7\3\2\2\2QO\3\2\2\2RS\b\5\1\2ST\5")
        buf.write(u"\22\n\2TU\5\b\5\6U`\3\2\2\2VW\7\3\2\2WX\5\b\5\2XY\7\4")
        buf.write(u"\2\2Y`\3\2\2\2Z`\5\24\13\2[\\\5\n\6\2\\]\5\f\7\2]^\5")
        buf.write(u"\n\6\2^`\3\2\2\2_R\3\2\2\2_V\3\2\2\2_Z\3\2\2\2_[\3\2")
        buf.write(u"\2\2`g\3\2\2\2ab\f\7\2\2bc\5\20\t\2cd\5\b\5\bdf\3\2\2")
        buf.write(u"\2ea\3\2\2\2fi\3\2\2\2ge\3\2\2\2gh\3\2\2\2h\t\3\2\2\2")
        buf.write(u"ig\3\2\2\2jw\7\32\2\2kl\7\t\2\2lm\7\31\2\2mw\7\7\2\2")
        buf.write(u"no\7\n\2\2op\7\31\2\2pq\7\6\2\2qr\7\31\2\2rw\7\7\2\2")
        buf.write(u"st\7\n\2\2tu\7\31\2\2uw\7\7\2\2vj\3\2\2\2vk\3\2\2\2v")
        buf.write(u"n\3\2\2\2vs\3\2\2\2w\13\3\2\2\2xy\t\2\2\2y\r\3\2\2\2")
        buf.write(u"z{\t\3\2\2{\17\3\2\2\2|}\t\4\2\2}\21\3\2\2\2~\177\7\r")
        buf.write(u"\2\2\177\23\3\2\2\2\u0080\u0081\7\16\2\2\u0081\25\3\2")
        buf.write(u"\2\2\n#+:BO_gv")
        return buf.getvalue()


class SpecificationGrammarParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'('", u"')'", u"'DC['", u"':'", u"']'", 
                     u"';'", u"'INTERFACE['", u"'CLASS['", u"'and'", u"'or'", 
                     u"'not'", u"'true'", u"'false'", u"'<='", u"'='", u"'>='", 
                     u"'<'", u"'>'", u"'!='", u"'+'", u"'-'", u"'*'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"AND", u"OR", u"NOT", u"TRUE", u"FALSE", 
                      u"LEQ", u"EQ", u"GEQ", u"LT", u"GT", u"NEQ", u"PLUS", 
                      u"MINUS", u"TIMES", u"ID", u"INT", u"WS" ]

    RULE_spec = 0
    RULE_expr = 1
    RULE_resourceFilter = 2
    RULE_specNoDC = 3
    RULE_exprNoDC = 4
    RULE_op = 5
    RULE_arithmetic_op = 6
    RULE_bool2Op = 7
    RULE_bool1Op = 8
    RULE_boolFact = 9

    ruleNames =  [ u"spec", u"expr", u"resourceFilter", u"specNoDC", u"exprNoDC", 
                   u"op", u"arithmetic_op", u"bool2Op", u"bool1Op", u"boolFact" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    AND=9
    OR=10
    NOT=11
    TRUE=12
    FALSE=13
    LEQ=14
    EQ=15
    GEQ=16
    LT=17
    GT=18
    NEQ=19
    PLUS=20
    MINUS=21
    TIMES=22
    ID=23
    INT=24
    WS=25

    def __init__(self, input):
        super(SpecificationGrammarParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class SpecContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SpecificationGrammarParser.SpecContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SpecificationGrammarParser.RULE_spec

     
        def copyFrom(self, ctx):
            super(SpecificationGrammarParser.SpecContext, self).copyFrom(ctx)


    class AspecBool2OpContext(SpecContext):

        def __init__(self, parser, ctx): # actually a SpecificationGrammarParser.SpecContext)
            super(SpecificationGrammarParser.AspecBool2OpContext, self).__init__(parser)
            self.copyFrom(ctx)

        def spec(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SpecificationGrammarParser.SpecContext)
            else:
                return self.getTypedRuleContext(SpecificationGrammarParser.SpecContext,i)

        def bool2Op(self):
            return self.getTypedRuleContext(SpecificationGrammarParser.Bool2OpContext,0)


        def accept(self, visitor):
            if isinstance( visitor, SpecificationGrammarVisitor ):
                return visitor.visitAspecBool2Op(self)
            else:
                return visitor.visitChildren(self)


    class AspecBracketsContext(SpecContext):

        def __init__(self, parser, ctx): # actually a SpecificationGrammarParser.SpecContext)
            super(SpecificationGrammarParser.AspecBracketsContext, self).__init__(parser)
            self.copyFrom(ctx)

        def spec(self):
            return self.getTypedRuleContext(SpecificationGrammarParser.SpecContext,0)


        def accept(self, visitor):
            if isinstance( visitor, SpecificationGrammarVisitor ):
                return visitor.visitAspecBrackets(self)
            else:
                return visitor.visitChildren(self)


    class AspecBool1OpContext(SpecContext):

        def __init__(self, parser, ctx): # actually a SpecificationGrammarParser.SpecContext)
            super(SpecificationGrammarParser.AspecBool1OpContext, self).__init__(parser)
            self.copyFrom(ctx)

        def bool1Op(self):
            return self.getTypedRuleContext(SpecificationGrammarParser.Bool1OpContext,0)

        def spec(self):
            return self.getTypedRuleContext(SpecificationGrammarParser.SpecContext,0)


        def accept(self, visitor):
            if isinstance( visitor, SpecificationGrammarVisitor ):
                return visitor.visitAspecBool1Op(self)
            else:
                return visitor.visitChildren(self)


    class AspecOpContext(SpecContext):

        def __init__(self, parser, ctx): # actually a SpecificationGrammarParser.SpecContext)
            super(SpecificationGrammarParser.AspecOpContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SpecificationGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(SpecificationGrammarParser.ExprContext,i)

        def op(self):
            return self.getTypedRuleContext(SpecificationGrammarParser.OpContext,0)


        def accept(self, visitor):
            if isinstance( visitor, SpecificationGrammarVisitor ):
                return visitor.visitAspecOp(self)
            else:
                return visitor.visitChildren(self)


    class AspecBoolFactContext(SpecContext):

        def __init__(self, parser, ctx): # actually a SpecificationGrammarParser.SpecContext)
            super(SpecificationGrammarParser.AspecBoolFactContext, self).__init__(parser)
            self.copyFrom(ctx)

        def boolFact(self):
            return self.getTypedRuleContext(SpecificationGrammarParser.BoolFactContext,0)


        def accept(self, visitor):
            if isinstance( visitor, SpecificationGrammarVisitor ):
                return visitor.visitAspecBoolFact(self)
            else:
                return visitor.visitChildren(self)



    def spec(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SpecificationGrammarParser.SpecContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_spec, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            token = self._input.LA(1)
            if token in [SpecificationGrammarParser.NOT]:
                localctx = SpecificationGrammarParser.AspecBool1OpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 21
                self.bool1Op()
                self.state = 22
                self.spec(4)

            elif token in [SpecificationGrammarParser.T__0]:
                localctx = SpecificationGrammarParser.AspecBracketsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 24
                self.match(SpecificationGrammarParser.T__0)
                self.state = 25
                self.spec(0)
                self.state = 26
                self.match(SpecificationGrammarParser.T__1)

            elif token in [SpecificationGrammarParser.TRUE]:
                localctx = SpecificationGrammarParser.AspecBoolFactContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 28
                self.boolFact()

            elif token in [SpecificationGrammarParser.T__2, SpecificationGrammarParser.T__6, SpecificationGrammarParser.T__7, SpecificationGrammarParser.INT]:
                localctx = SpecificationGrammarParser.AspecOpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 29
                self.expr(0)
                self.state = 30
                self.op()
                self.state = 31
                self.expr(0)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 41
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SpecificationGrammarParser.AspecBool2OpContext(self, SpecificationGrammarParser.SpecContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_spec)
                    self.state = 35
                    if not self.precpred(self._ctx, 5):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                    self.state = 36
                    self.bool2Op()
                    self.state = 37
                    self.spec(6) 
                self.state = 43
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SpecificationGrammarParser.ExprContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SpecificationGrammarParser.RULE_expr

     
        def copyFrom(self, ctx):
            super(SpecificationGrammarParser.ExprContext, self).copyFrom(ctx)


    class AexprDCContext(ExprContext):

        def __init__(self, parser, ctx): # actually a SpecificationGrammarParser.ExprContext)
            super(SpecificationGrammarParser.AexprDCContext, self).__init__(parser)
            self.copyFrom(ctx)

        def resourceFilter(self):
            return self.getTypedRuleContext(SpecificationGrammarParser.ResourceFilterContext,0)

        def specNoDC(self):
            return self.getTypedRuleContext(SpecificationGrammarParser.SpecNoDCContext,0)


        def accept(self, visitor):
            if isinstance( visitor, SpecificationGrammarVisitor ):
                return visitor.visitAexprDC(self)
            else:
                return visitor.visitChildren(self)


    class AexprDCNoFilterContext(ExprContext):

        def __init__(self, parser, ctx): # actually a SpecificationGrammarParser.ExprContext)
            super(SpecificationGrammarParser.AexprDCNoFilterContext, self).__init__(parser)
            self.copyFrom(ctx)

        def specNoDC(self):
            return self.getTypedRuleContext(SpecificationGrammarParser.SpecNoDCContext,0)


        def accept(self, visitor):
            if isinstance( visitor, SpecificationGrammarVisitor ):
                return visitor.visitAexprDCNoFilter(self)
            else:
                return visitor.visitChildren(self)


    class AexprNoDCContext(ExprContext):

        def __init__(self, parser, ctx): # actually a SpecificationGrammarParser.ExprContext)
            super(SpecificationGrammarParser.AexprNoDCContext, self).__init__(parser)
            self.copyFrom(ctx)

        def exprNoDC(self):
            return self.getTypedRuleContext(SpecificationGrammarParser.ExprNoDCContext,0)


        def accept(self, visitor):
            if isinstance( visitor, SpecificationGrammarVisitor ):
                return visitor.visitAexprNoDC(self)
            else:
                return visitor.visitChildren(self)


    class AexprArithmeticContext(ExprContext):

        def __init__(self, parser, ctx): # actually a SpecificationGrammarParser.ExprContext)
            super(SpecificationGrammarParser.AexprArithmeticContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SpecificationGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(SpecificationGrammarParser.ExprContext,i)

        def arithmetic_op(self):
            return self.getTypedRuleContext(SpecificationGrammarParser.Arithmetic_opContext,0)


        def accept(self, visitor):
            if isinstance( visitor, SpecificationGrammarVisitor ):
                return visitor.visitAexprArithmetic(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SpecificationGrammarParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = SpecificationGrammarParser.AexprDCContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 45
                self.match(SpecificationGrammarParser.T__2)
                self.state = 46
                self.resourceFilter(0)
                self.state = 47
                self.match(SpecificationGrammarParser.T__3)
                self.state = 48
                self.specNoDC(0)
                self.state = 49
                self.match(SpecificationGrammarParser.T__4)
                pass

            elif la_ == 2:
                localctx = SpecificationGrammarParser.AexprDCNoFilterContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 51
                self.match(SpecificationGrammarParser.T__2)
                self.state = 52
                self.specNoDC(0)
                self.state = 53
                self.match(SpecificationGrammarParser.T__4)
                pass

            elif la_ == 3:
                localctx = SpecificationGrammarParser.AexprNoDCContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 55
                self.exprNoDC()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 64
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SpecificationGrammarParser.AexprArithmeticContext(self, SpecificationGrammarParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 58
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 59
                    self.arithmetic_op()
                    self.state = 60
                    self.expr(3) 
                self.state = 66
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ResourceFilterContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SpecificationGrammarParser.ResourceFilterContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SpecificationGrammarParser.RULE_resourceFilter

     
        def copyFrom(self, ctx):
            super(SpecificationGrammarParser.ResourceFilterContext, self).copyFrom(ctx)


    class AresourceFilterOpContext(ResourceFilterContext):

        def __init__(self, parser, ctx): # actually a SpecificationGrammarParser.ResourceFilterContext)
            super(SpecificationGrammarParser.AresourceFilterOpContext, self).__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SpecificationGrammarParser.ID, 0)
        def op(self):
            return self.getTypedRuleContext(SpecificationGrammarParser.OpContext,0)

        def INT(self):
            return self.getToken(SpecificationGrammarParser.INT, 0)

        def accept(self, visitor):
            if isinstance( visitor, SpecificationGrammarVisitor ):
                return visitor.visitAresourceFilterOp(self)
            else:
                return visitor.visitChildren(self)


    class AresourceFilterBool2OpContext(ResourceFilterContext):

        def __init__(self, parser, ctx): # actually a SpecificationGrammarParser.ResourceFilterContext)
            super(SpecificationGrammarParser.AresourceFilterBool2OpContext, self).__init__(parser)
            self.copyFrom(ctx)

        def resourceFilter(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SpecificationGrammarParser.ResourceFilterContext)
            else:
                return self.getTypedRuleContext(SpecificationGrammarParser.ResourceFilterContext,i)


        def accept(self, visitor):
            if isinstance( visitor, SpecificationGrammarVisitor ):
                return visitor.visitAresourceFilterBool2Op(self)
            else:
                return visitor.visitChildren(self)



    def resourceFilter(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SpecificationGrammarParser.ResourceFilterContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_resourceFilter, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SpecificationGrammarParser.AresourceFilterOpContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 68
            self.match(SpecificationGrammarParser.ID)
            self.state = 69
            self.op()
            self.state = 70
            self.match(SpecificationGrammarParser.INT)
            self._ctx.stop = self._input.LT(-1)
            self.state = 77
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SpecificationGrammarParser.AresourceFilterBool2OpContext(self, SpecificationGrammarParser.ResourceFilterContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_resourceFilter)
                    self.state = 72
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 73
                    self.match(SpecificationGrammarParser.T__5)
                    self.state = 74
                    self.resourceFilter(2) 
                self.state = 79
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class SpecNoDCContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SpecificationGrammarParser.SpecNoDCContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SpecificationGrammarParser.RULE_specNoDC

     
        def copyFrom(self, ctx):
            super(SpecificationGrammarParser.SpecNoDCContext, self).copyFrom(ctx)


    class AspecNoDCOpContext(SpecNoDCContext):

        def __init__(self, parser, ctx): # actually a SpecificationGrammarParser.SpecNoDCContext)
            super(SpecificationGrammarParser.AspecNoDCOpContext, self).__init__(parser)
            self.copyFrom(ctx)

        def exprNoDC(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SpecificationGrammarParser.ExprNoDCContext)
            else:
                return self.getTypedRuleContext(SpecificationGrammarParser.ExprNoDCContext,i)

        def op(self):
            return self.getTypedRuleContext(SpecificationGrammarParser.OpContext,0)


        def accept(self, visitor):
            if isinstance( visitor, SpecificationGrammarVisitor ):
                return visitor.visitAspecNoDCOp(self)
            else:
                return visitor.visitChildren(self)


    class AspecNoDCBool2OpContext(SpecNoDCContext):

        def __init__(self, parser, ctx): # actually a SpecificationGrammarParser.SpecNoDCContext)
            super(SpecificationGrammarParser.AspecNoDCBool2OpContext, self).__init__(parser)
            self.copyFrom(ctx)

        def specNoDC(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SpecificationGrammarParser.SpecNoDCContext)
            else:
                return self.getTypedRuleContext(SpecificationGrammarParser.SpecNoDCContext,i)

        def bool2Op(self):
            return self.getTypedRuleContext(SpecificationGrammarParser.Bool2OpContext,0)


        def accept(self, visitor):
            if isinstance( visitor, SpecificationGrammarVisitor ):
                return visitor.visitAspecNoDCBool2Op(self)
            else:
                return visitor.visitChildren(self)


    class AspecNoDCBool1OpContext(SpecNoDCContext):

        def __init__(self, parser, ctx): # actually a SpecificationGrammarParser.SpecNoDCContext)
            super(SpecificationGrammarParser.AspecNoDCBool1OpContext, self).__init__(parser)
            self.copyFrom(ctx)

        def bool1Op(self):
            return self.getTypedRuleContext(SpecificationGrammarParser.Bool1OpContext,0)

        def specNoDC(self):
            return self.getTypedRuleContext(SpecificationGrammarParser.SpecNoDCContext,0)


        def accept(self, visitor):
            if isinstance( visitor, SpecificationGrammarVisitor ):
                return visitor.visitAspecNoDCBool1Op(self)
            else:
                return visitor.visitChildren(self)


    class AspecNoDCBoolFactContext(SpecNoDCContext):

        def __init__(self, parser, ctx): # actually a SpecificationGrammarParser.SpecNoDCContext)
            super(SpecificationGrammarParser.AspecNoDCBoolFactContext, self).__init__(parser)
            self.copyFrom(ctx)

        def boolFact(self):
            return self.getTypedRuleContext(SpecificationGrammarParser.BoolFactContext,0)


        def accept(self, visitor):
            if isinstance( visitor, SpecificationGrammarVisitor ):
                return visitor.visitAspecNoDCBoolFact(self)
            else:
                return visitor.visitChildren(self)


    class AspecNoDCBracketsContext(SpecNoDCContext):

        def __init__(self, parser, ctx): # actually a SpecificationGrammarParser.SpecNoDCContext)
            super(SpecificationGrammarParser.AspecNoDCBracketsContext, self).__init__(parser)
            self.copyFrom(ctx)

        def specNoDC(self):
            return self.getTypedRuleContext(SpecificationGrammarParser.SpecNoDCContext,0)


        def accept(self, visitor):
            if isinstance( visitor, SpecificationGrammarVisitor ):
                return visitor.visitAspecNoDCBrackets(self)
            else:
                return visitor.visitChildren(self)



    def specNoDC(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SpecificationGrammarParser.SpecNoDCContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_specNoDC, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            token = self._input.LA(1)
            if token in [SpecificationGrammarParser.NOT]:
                localctx = SpecificationGrammarParser.AspecNoDCBool1OpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 81
                self.bool1Op()
                self.state = 82
                self.specNoDC(4)

            elif token in [SpecificationGrammarParser.T__0]:
                localctx = SpecificationGrammarParser.AspecNoDCBracketsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 84
                self.match(SpecificationGrammarParser.T__0)
                self.state = 85
                self.specNoDC(0)
                self.state = 86
                self.match(SpecificationGrammarParser.T__1)

            elif token in [SpecificationGrammarParser.TRUE]:
                localctx = SpecificationGrammarParser.AspecNoDCBoolFactContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 88
                self.boolFact()

            elif token in [SpecificationGrammarParser.T__6, SpecificationGrammarParser.T__7, SpecificationGrammarParser.INT]:
                localctx = SpecificationGrammarParser.AspecNoDCOpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 89
                self.exprNoDC()
                self.state = 90
                self.op()
                self.state = 91
                self.exprNoDC()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 101
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SpecificationGrammarParser.AspecNoDCBool2OpContext(self, SpecificationGrammarParser.SpecNoDCContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_specNoDC)
                    self.state = 95
                    if not self.precpred(self._ctx, 5):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                    self.state = 96
                    self.bool2Op()
                    self.state = 97
                    self.specNoDC(6) 
                self.state = 103
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ExprNoDCContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SpecificationGrammarParser.ExprNoDCContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SpecificationGrammarParser.RULE_exprNoDC

     
        def copyFrom(self, ctx):
            super(SpecificationGrammarParser.ExprNoDCContext, self).copyFrom(ctx)



    class AexprNoDCClassScenarioContext(ExprNoDCContext):

        def __init__(self, parser, ctx): # actually a SpecificationGrammarParser.ExprNoDCContext)
            super(SpecificationGrammarParser.AexprNoDCClassScenarioContext, self).__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i=None):
            if i is None:
                return self.getTokens(SpecificationGrammarParser.ID)
            else:
                return self.getToken(SpecificationGrammarParser.ID, i)

        def accept(self, visitor):
            if isinstance( visitor, SpecificationGrammarVisitor ):
                return visitor.visitAexprNoDCClassScenario(self)
            else:
                return visitor.visitChildren(self)


    class AexprNoDCClassContext(ExprNoDCContext):

        def __init__(self, parser, ctx): # actually a SpecificationGrammarParser.ExprNoDCContext)
            super(SpecificationGrammarParser.AexprNoDCClassContext, self).__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SpecificationGrammarParser.ID, 0)

        def accept(self, visitor):
            if isinstance( visitor, SpecificationGrammarVisitor ):
                return visitor.visitAexprNoDCClass(self)
            else:
                return visitor.visitChildren(self)


    class AexprNoDCIntContext(ExprNoDCContext):

        def __init__(self, parser, ctx): # actually a SpecificationGrammarParser.ExprNoDCContext)
            super(SpecificationGrammarParser.AexprNoDCIntContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(SpecificationGrammarParser.INT, 0)

        def accept(self, visitor):
            if isinstance( visitor, SpecificationGrammarVisitor ):
                return visitor.visitAexprNoDCInt(self)
            else:
                return visitor.visitChildren(self)


    class AexprNoDCInterfaceContext(ExprNoDCContext):

        def __init__(self, parser, ctx): # actually a SpecificationGrammarParser.ExprNoDCContext)
            super(SpecificationGrammarParser.AexprNoDCInterfaceContext, self).__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SpecificationGrammarParser.ID, 0)

        def accept(self, visitor):
            if isinstance( visitor, SpecificationGrammarVisitor ):
                return visitor.visitAexprNoDCInterface(self)
            else:
                return visitor.visitChildren(self)



    def exprNoDC(self):

        localctx = SpecificationGrammarParser.ExprNoDCContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_exprNoDC)
        try:
            self.state = 116
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = SpecificationGrammarParser.AexprNoDCIntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.match(SpecificationGrammarParser.INT)
                pass

            elif la_ == 2:
                localctx = SpecificationGrammarParser.AexprNoDCInterfaceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.match(SpecificationGrammarParser.T__6)
                self.state = 106
                self.match(SpecificationGrammarParser.ID)
                self.state = 107
                self.match(SpecificationGrammarParser.T__4)
                pass

            elif la_ == 3:
                localctx = SpecificationGrammarParser.AexprNoDCClassScenarioContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 108
                self.match(SpecificationGrammarParser.T__7)
                self.state = 109
                self.match(SpecificationGrammarParser.ID)
                self.state = 110
                self.match(SpecificationGrammarParser.T__3)
                self.state = 111
                self.match(SpecificationGrammarParser.ID)
                self.state = 112
                self.match(SpecificationGrammarParser.T__4)
                pass

            elif la_ == 4:
                localctx = SpecificationGrammarParser.AexprNoDCClassContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 113
                self.match(SpecificationGrammarParser.T__7)
                self.state = 114
                self.match(SpecificationGrammarParser.ID)
                self.state = 115
                self.match(SpecificationGrammarParser.T__4)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OpContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SpecificationGrammarParser.OpContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LEQ(self):
            return self.getToken(SpecificationGrammarParser.LEQ, 0)

        def EQ(self):
            return self.getToken(SpecificationGrammarParser.EQ, 0)

        def GEQ(self):
            return self.getToken(SpecificationGrammarParser.GEQ, 0)

        def LT(self):
            return self.getToken(SpecificationGrammarParser.LT, 0)

        def GT(self):
            return self.getToken(SpecificationGrammarParser.GT, 0)

        def NEQ(self):
            return self.getToken(SpecificationGrammarParser.NEQ, 0)

        def getRuleIndex(self):
            return SpecificationGrammarParser.RULE_op

        def accept(self, visitor):
            if isinstance( visitor, SpecificationGrammarVisitor ):
                return visitor.visitOp(self)
            else:
                return visitor.visitChildren(self)




    def op(self):

        localctx = SpecificationGrammarParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SpecificationGrammarParser.LEQ) | (1 << SpecificationGrammarParser.EQ) | (1 << SpecificationGrammarParser.GEQ) | (1 << SpecificationGrammarParser.LT) | (1 << SpecificationGrammarParser.GT) | (1 << SpecificationGrammarParser.NEQ))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Arithmetic_opContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SpecificationGrammarParser.Arithmetic_opContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(SpecificationGrammarParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(SpecificationGrammarParser.MINUS, 0)

        def TIMES(self):
            return self.getToken(SpecificationGrammarParser.TIMES, 0)

        def getRuleIndex(self):
            return SpecificationGrammarParser.RULE_arithmetic_op

        def accept(self, visitor):
            if isinstance( visitor, SpecificationGrammarVisitor ):
                return visitor.visitArithmetic_op(self)
            else:
                return visitor.visitChildren(self)




    def arithmetic_op(self):

        localctx = SpecificationGrammarParser.Arithmetic_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_arithmetic_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SpecificationGrammarParser.PLUS) | (1 << SpecificationGrammarParser.MINUS) | (1 << SpecificationGrammarParser.TIMES))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Bool2OpContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SpecificationGrammarParser.Bool2OpContext, self).__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(SpecificationGrammarParser.AND, 0)

        def OR(self):
            return self.getToken(SpecificationGrammarParser.OR, 0)

        def getRuleIndex(self):
            return SpecificationGrammarParser.RULE_bool2Op

        def accept(self, visitor):
            if isinstance( visitor, SpecificationGrammarVisitor ):
                return visitor.visitBool2Op(self)
            else:
                return visitor.visitChildren(self)




    def bool2Op(self):

        localctx = SpecificationGrammarParser.Bool2OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_bool2Op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            _la = self._input.LA(1)
            if not(_la==SpecificationGrammarParser.AND or _la==SpecificationGrammarParser.OR):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Bool1OpContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SpecificationGrammarParser.Bool1OpContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(SpecificationGrammarParser.NOT, 0)

        def getRuleIndex(self):
            return SpecificationGrammarParser.RULE_bool1Op

        def accept(self, visitor):
            if isinstance( visitor, SpecificationGrammarVisitor ):
                return visitor.visitBool1Op(self)
            else:
                return visitor.visitChildren(self)




    def bool1Op(self):

        localctx = SpecificationGrammarParser.Bool1OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_bool1Op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(SpecificationGrammarParser.NOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BoolFactContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SpecificationGrammarParser.BoolFactContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(SpecificationGrammarParser.TRUE, 0)

        def getRuleIndex(self):
            return SpecificationGrammarParser.RULE_boolFact

        def accept(self, visitor):
            if isinstance( visitor, SpecificationGrammarVisitor ):
                return visitor.visitBoolFact(self)
            else:
                return visitor.visitChildren(self)




    def boolFact(self):

        localctx = SpecificationGrammarParser.BoolFactContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_boolFact)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(SpecificationGrammarParser.TRUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.spec_sempred
        self._predicates[1] = self.expr_sempred
        self._predicates[2] = self.resourceFilter_sempred
        self._predicates[3] = self.specNoDC_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def spec_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

    def expr_sempred(self, localctx, predIndex):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def resourceFilter_sempred(self, localctx, predIndex):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def specNoDC_sempred(self, localctx, predIndex):
            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         



