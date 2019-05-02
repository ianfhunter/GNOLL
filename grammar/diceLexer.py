# Generated from dice.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write(";\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6)")
        buf.write("\n\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\6\f")
        buf.write("\66\n\f\r\f\16\f\67\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\2\3\2\2\2>\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\3\33\3\2\2\2\5\35\3\2\2\2\7\37")
        buf.write("\3\2\2\2\t!\3\2\2\2\13(\3\2\2\2\r*\3\2\2\2\17,\3\2\2\2")
        buf.write("\21.\3\2\2\2\23\60\3\2\2\2\25\62\3\2\2\2\27\65\3\2\2\2")
        buf.write("\319\3\2\2\2\33\34\7f\2\2\34\4\3\2\2\2\35\36\7J\2\2\36")
        buf.write("\6\3\2\2\2\37 \7N\2\2 \b\3\2\2\2!\"\7H\2\2\"\n\3\2\2\2")
        buf.write("#)\5\r\7\2$)\5\17\b\2%)\5\21\t\2&)\5\23\n\2\')\5\25\13")
        buf.write("\2(#\3\2\2\2($\3\2\2\2(%\3\2\2\2(&\3\2\2\2(\'\3\2\2\2")
        buf.write(")\f\3\2\2\2*+\7-\2\2+\16\3\2\2\2,-\7/\2\2-\20\3\2\2\2")
        buf.write("./\7,\2\2/\22\3\2\2\2\60\61\7\61\2\2\61\24\3\2\2\2\62")
        buf.write("\63\7z\2\2\63\26\3\2\2\2\64\66\5\31\r\2\65\64\3\2\2\2")
        buf.write("\66\67\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28\30\3\2\2\29")
        buf.write(":\4\62;\2:\32\3\2\2\2\5\2(\67\2")
        return buf.getvalue()


class diceLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    FATE = 4
    OPERATOR = 5
    PLUS = 6
    MINUS = 7
    MULT = 8
    DIV = 9
    SEVERAL = 10
    INTEGER_NUMBER = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'d'", "'H'", "'L'", "'F'", "'+'", "'-'", "'*'", "'/'", "'x'" ]

    symbolicNames = [ "<INVALID>",
            "FATE", "OPERATOR", "PLUS", "MINUS", "MULT", "DIV", "SEVERAL", 
            "INTEGER_NUMBER" ]

    ruleNames = [ "T__0", "T__1", "T__2", "FATE", "OPERATOR", "PLUS", "MINUS", 
                  "MULT", "DIV", "SEVERAL", "INTEGER_NUMBER", "DIGIT" ]

    grammarFileName = "dice.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


