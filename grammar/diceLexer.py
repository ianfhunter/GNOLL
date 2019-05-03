# Generated from dice.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("H\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6\60\n\6\3\7\3\7\3\b\3")
        buf.write("\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16")
        buf.write("\3\17\6\17C\n\17\r\17\16\17D\3\20\3\20\2\2\21\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\2\3\2\2\2L\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3!\3\2\2\2\5#\3\2\2")
        buf.write("\2\7%\3\2\2\2\t\'\3\2\2\2\13/\3\2\2\2\r\61\3\2\2\2\17")
        buf.write("\63\3\2\2\2\21\65\3\2\2\2\23\67\3\2\2\2\259\3\2\2\2\27")
        buf.write(";\3\2\2\2\31=\3\2\2\2\33?\3\2\2\2\35B\3\2\2\2\37F\3\2")
        buf.write("\2\2!\"\7f\2\2\"\4\3\2\2\2#$\7J\2\2$\6\3\2\2\2%&\7N\2")
        buf.write("\2&\b\3\2\2\2\'(\7H\2\2(\n\3\2\2\2)\60\5\r\7\2*\60\5\17")
        buf.write("\b\2+\60\5\21\t\2,\60\5\23\n\2-\60\5\25\13\2.\60\5\27")
        buf.write("\f\2/)\3\2\2\2/*\3\2\2\2/+\3\2\2\2/,\3\2\2\2/-\3\2\2\2")
        buf.write("/.\3\2\2\2\60\f\3\2\2\2\61\62\7-\2\2\62\16\3\2\2\2\63")
        buf.write("\64\7/\2\2\64\20\3\2\2\2\65\66\7,\2\2\66\22\3\2\2\2\67")
        buf.write("8\7\61\2\28\24\3\2\2\29:\7~\2\2:\26\3\2\2\2;<\7z\2\2<")
        buf.write("\30\3\2\2\2=>\7*\2\2>\32\3\2\2\2?@\7+\2\2@\34\3\2\2\2")
        buf.write("AC\5\37\20\2BA\3\2\2\2CD\3\2\2\2DB\3\2\2\2DE\3\2\2\2E")
        buf.write("\36\3\2\2\2FG\4\62;\2G \3\2\2\2\5\2/D\2")
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
    DIV_RUP = 10
    SEVERAL = 11
    OPEN_BRACKET = 12
    CLOSE_BRACKET = 13
    INTEGER_NUMBER = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'d'", "'H'", "'L'", "'F'", "'+'", "'-'", "'*'", "'/'", "'|'", 
            "'x'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "FATE", "OPERATOR", "PLUS", "MINUS", "MULT", "DIV", "DIV_RUP", 
            "SEVERAL", "OPEN_BRACKET", "CLOSE_BRACKET", "INTEGER_NUMBER" ]

    ruleNames = [ "T__0", "T__1", "T__2", "FATE", "OPERATOR", "PLUS", "MINUS", 
                  "MULT", "DIV", "DIV_RUP", "SEVERAL", "OPEN_BRACKET", "CLOSE_BRACKET", 
                  "INTEGER_NUMBER", "DIGIT" ]

    grammarFileName = "dice.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


