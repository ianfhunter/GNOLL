# Generated from dice.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("G\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\5\2\26\n\2\3\2\7\2\31\n\2\f\2")
        buf.write("\16\2\34\13\2\3\2\5\2\37\n\2\3\3\3\3\5\3#\n\3\3\3\3\3")
        buf.write("\5\3\'\n\3\3\3\7\3*\n\3\f\3\16\3-\13\3\3\4\5\4\60\n\4")
        buf.write("\3\4\3\4\3\4\3\4\5\4\66\n\4\3\5\3\5\3\6\3\6\3\6\5\6=\n")
        buf.write("\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\2\2\13\2\4\6\b")
        buf.write("\n\f\16\20\22\2\2\2F\2\25\3\2\2\2\4 \3\2\2\2\6\65\3\2")
        buf.write("\2\2\b\67\3\2\2\2\n9\3\2\2\2\f>\3\2\2\2\16@\3\2\2\2\20")
        buf.write("B\3\2\2\2\22D\3\2\2\2\24\26\7\22\2\2\25\24\3\2\2\2\25")
        buf.write("\26\3\2\2\2\26\32\3\2\2\2\27\31\5\4\3\2\30\27\3\2\2\2")
        buf.write("\31\34\3\2\2\2\32\30\3\2\2\2\32\33\3\2\2\2\33\36\3\2\2")
        buf.write("\2\34\32\3\2\2\2\35\37\7\22\2\2\36\35\3\2\2\2\36\37\3")
        buf.write("\2\2\2\37\3\3\2\2\2 +\5\6\4\2!#\7\22\2\2\"!\3\2\2\2\"")
        buf.write("#\3\2\2\2#$\3\2\2\2$&\7\7\2\2%\'\7\22\2\2&%\3\2\2\2&\'")
        buf.write("\3\2\2\2\'(\3\2\2\2(*\5\4\3\2)\"\3\2\2\2*-\3\2\2\2+)\3")
        buf.write("\2\2\2+,\3\2\2\2,\5\3\2\2\2-+\3\2\2\2.\60\5\20\t\2/.\3")
        buf.write("\2\2\2/\60\3\2\2\2\60\61\3\2\2\2\61\62\5\b\5\2\62\63\5")
        buf.write("\22\n\2\63\66\3\2\2\2\64\66\5\20\t\2\65/\3\2\2\2\65\64")
        buf.write("\3\2\2\2\66\7\3\2\2\2\678\7\3\2\28\t\3\2\2\29<\5\20\t")
        buf.write("\2:=\5\f\7\2;=\5\16\b\2<:\3\2\2\2<;\3\2\2\2=\13\3\2\2")
        buf.write("\2>?\7\4\2\2?\r\3\2\2\2@A\7\5\2\2A\17\3\2\2\2BC\7\21\2")
        buf.write("\2C\21\3\2\2\2DE\7\21\2\2E\23\3\2\2\2\13\25\32\36\"&+")
        buf.write("/\65<")
        return buf.getvalue()


class diceParser ( Parser ):

    grammarFileName = "dice.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'d'", "'H'", "'L'", "'F'", "<INVALID>", 
                     "'+'", "'^'", "'-'", "'*'", "'/'", "'|'", "'x'", "'('", 
                     "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "FATE", "OPERATOR", "PLUS", "POWER", "MINUS", "MULT", 
                      "DIV", "DIV_RUP", "SEVERAL", "OPEN_BRACKET", "CLOSE_BRACKET", 
                      "INTEGER_NUMBER", "WSPACE" ]

    RULE_schema = 0
    RULE_dice_roll = 1
    RULE_die_roll = 2
    RULE_die = 3
    RULE_subset = 4
    RULE_highest = 5
    RULE_lowest = 6
    RULE_amount = 7
    RULE_faces = 8

    ruleNames =  [ "schema", "dice_roll", "die_roll", "die", "subset", "highest", 
                   "lowest", "amount", "faces" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    FATE=4
    OPERATOR=5
    PLUS=6
    POWER=7
    MINUS=8
    MULT=9
    DIV=10
    DIV_RUP=11
    SEVERAL=12
    OPEN_BRACKET=13
    CLOSE_BRACKET=14
    INTEGER_NUMBER=15
    WSPACE=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class SchemaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WSPACE(self, i:int=None):
            if i is None:
                return self.getTokens(diceParser.WSPACE)
            else:
                return self.getToken(diceParser.WSPACE, i)

        def dice_roll(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(diceParser.Dice_rollContext)
            else:
                return self.getTypedRuleContext(diceParser.Dice_rollContext,i)


        def getRuleIndex(self):
            return diceParser.RULE_schema

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSchema" ):
                listener.enterSchema(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSchema" ):
                listener.exitSchema(self)




    def schema(self):

        localctx = diceParser.SchemaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_schema)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 18
                self.match(diceParser.WSPACE)


            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==diceParser.T__0 or _la==diceParser.INTEGER_NUMBER:
                self.state = 21
                self.dice_roll()
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==diceParser.WSPACE:
                self.state = 27
                self.match(diceParser.WSPACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dice_rollContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def die_roll(self):
            return self.getTypedRuleContext(diceParser.Die_rollContext,0)


        def OPERATOR(self, i:int=None):
            if i is None:
                return self.getTokens(diceParser.OPERATOR)
            else:
                return self.getToken(diceParser.OPERATOR, i)

        def dice_roll(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(diceParser.Dice_rollContext)
            else:
                return self.getTypedRuleContext(diceParser.Dice_rollContext,i)


        def WSPACE(self, i:int=None):
            if i is None:
                return self.getTokens(diceParser.WSPACE)
            else:
                return self.getToken(diceParser.WSPACE, i)

        def getRuleIndex(self):
            return diceParser.RULE_dice_roll

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDice_roll" ):
                listener.enterDice_roll(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDice_roll" ):
                listener.exitDice_roll(self)




    def dice_roll(self):

        localctx = diceParser.Dice_rollContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_dice_roll)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.die_roll()
            self.state = 41
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 32
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==diceParser.WSPACE:
                        self.state = 31
                        self.match(diceParser.WSPACE)


                    self.state = 34
                    self.match(diceParser.OPERATOR)
                    self.state = 36
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==diceParser.WSPACE:
                        self.state = 35
                        self.match(diceParser.WSPACE)


                    self.state = 38
                    self.dice_roll() 
                self.state = 43
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Die_rollContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def die(self):
            return self.getTypedRuleContext(diceParser.DieContext,0)


        def faces(self):
            return self.getTypedRuleContext(diceParser.FacesContext,0)


        def amount(self):
            return self.getTypedRuleContext(diceParser.AmountContext,0)


        def getRuleIndex(self):
            return diceParser.RULE_die_roll

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDie_roll" ):
                listener.enterDie_roll(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDie_roll" ):
                listener.exitDie_roll(self)




    def die_roll(self):

        localctx = diceParser.Die_rollContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_die_roll)
        self._la = 0 # Token type
        try:
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==diceParser.INTEGER_NUMBER:
                    self.state = 44
                    self.amount()


                self.state = 47
                self.die()
                self.state = 48
                self.faces()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.amount()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DieContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return diceParser.RULE_die

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDie" ):
                listener.enterDie(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDie" ):
                listener.exitDie(self)




    def die(self):

        localctx = diceParser.DieContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_die)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(diceParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubsetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def amount(self):
            return self.getTypedRuleContext(diceParser.AmountContext,0)


        def highest(self):
            return self.getTypedRuleContext(diceParser.HighestContext,0)


        def lowest(self):
            return self.getTypedRuleContext(diceParser.LowestContext,0)


        def getRuleIndex(self):
            return diceParser.RULE_subset

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubset" ):
                listener.enterSubset(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubset" ):
                listener.exitSubset(self)




    def subset(self):

        localctx = diceParser.SubsetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_subset)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.amount()
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [diceParser.T__1]:
                self.state = 56
                self.highest()
                pass
            elif token in [diceParser.T__2]:
                self.state = 57
                self.lowest()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class HighestContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return diceParser.RULE_highest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHighest" ):
                listener.enterHighest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHighest" ):
                listener.exitHighest(self)




    def highest(self):

        localctx = diceParser.HighestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_highest)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(diceParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LowestContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return diceParser.RULE_lowest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLowest" ):
                listener.enterLowest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLowest" ):
                listener.exitLowest(self)




    def lowest(self):

        localctx = diceParser.LowestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_lowest)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(diceParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AmountContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_NUMBER(self):
            return self.getToken(diceParser.INTEGER_NUMBER, 0)

        def getRuleIndex(self):
            return diceParser.RULE_amount

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAmount" ):
                listener.enterAmount(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAmount" ):
                listener.exitAmount(self)




    def amount(self):

        localctx = diceParser.AmountContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_amount)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(diceParser.INTEGER_NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FacesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_NUMBER(self):
            return self.getToken(diceParser.INTEGER_NUMBER, 0)

        def getRuleIndex(self):
            return diceParser.RULE_faces

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFaces" ):
                listener.enterFaces(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFaces" ):
                listener.exitFaces(self)




    def faces(self):

        localctx = diceParser.FacesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_faces)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(diceParser.INTEGER_NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





