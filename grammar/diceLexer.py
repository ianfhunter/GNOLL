# Generated from dice.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("P\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3")
        buf.write("\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\6")
        buf.write("\17A\n\17\r\17\16\17B\3\20\6\20F\n\20\r\20\16\20G\3\21")
        buf.write("\3\21\3\22\6\22M\n\22\r\22\16\22N\2\2\23\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\2#\2\3\2\3\4\2\13\13\"\"\2P\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\3%\3\2\2\2\5\'\3\2\2\2\7)\3\2\2\2\t+\3\2\2")
        buf.write("\2\13-\3\2\2\2\r/\3\2\2\2\17\61\3\2\2\2\21\63\3\2\2\2")
        buf.write("\23\65\3\2\2\2\25\67\3\2\2\2\279\3\2\2\2\31;\3\2\2\2\33")
        buf.write("=\3\2\2\2\35@\3\2\2\2\37E\3\2\2\2!I\3\2\2\2#L\3\2\2\2")
        buf.write("%&\7f\2\2&\4\3\2\2\2\'(\7J\2\2(\6\3\2\2\2)*\7N\2\2*\b")
        buf.write("\3\2\2\2+,\7H\2\2,\n\3\2\2\2-.\7-\2\2.\f\3\2\2\2/\60\7")
        buf.write("`\2\2\60\16\3\2\2\2\61\62\7/\2\2\62\20\3\2\2\2\63\64\7")
        buf.write(",\2\2\64\22\3\2\2\2\65\66\7\61\2\2\66\24\3\2\2\2\678\7")
        buf.write("~\2\28\26\3\2\2\29:\7z\2\2:\30\3\2\2\2;<\7*\2\2<\32\3")
        buf.write("\2\2\2=>\7+\2\2>\34\3\2\2\2?A\5!\21\2@?\3\2\2\2AB\3\2")
        buf.write("\2\2B@\3\2\2\2BC\3\2\2\2C\36\3\2\2\2DF\5#\22\2ED\3\2\2")
        buf.write("\2FG\3\2\2\2GE\3\2\2\2GH\3\2\2\2H \3\2\2\2IJ\4\62;\2J")
        buf.write("\"\3\2\2\2KM\t\2\2\2LK\3\2\2\2MN\3\2\2\2NL\3\2\2\2NO\3")
        buf.write("\2\2\2O$\3\2\2\2\6\2BGN\2")
        return buf.getvalue()


class diceLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    FATE = 4
    PLUS = 5
    POWER = 6
    MINUS = 7
    MULT = 8
    DIV = 9
    DIV_RUP = 10
    SEVERAL = 11
    OPEN_BRACKET = 12
    CLOSE_BRACKET = 13
    INTEGER_NUMBER = 14
    WSPACE = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'d'", "'H'", "'L'", "'F'", "'+'", "'^'", "'-'", "'*'", "'/'", 
            "'|'", "'x'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "FATE", "PLUS", "POWER", "MINUS", "MULT", "DIV", "DIV_RUP", 
            "SEVERAL", "OPEN_BRACKET", "CLOSE_BRACKET", "INTEGER_NUMBER", 
            "WSPACE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "FATE", "PLUS", "POWER", "MINUS", 
                  "MULT", "DIV", "DIV_RUP", "SEVERAL", "OPEN_BRACKET", "CLOSE_BRACKET", 
                  "INTEGER_NUMBER", "WSPACE", "DIGIT", "BLANK" ]

    grammarFileName = "dice.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


