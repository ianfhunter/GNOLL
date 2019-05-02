# Generated from dice.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("C\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\5\6-\n\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3")
        buf.write("\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\6\16>\n\16\r\16\16\16")
        buf.write("?\3\17\3\17\2\2\20\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\35\2\3\2\2\2F\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\37\3\2")
        buf.write("\2\2\5!\3\2\2\2\7#\3\2\2\2\t%\3\2\2\2\13,\3\2\2\2\r.\3")
        buf.write("\2\2\2\17\60\3\2\2\2\21\62\3\2\2\2\23\64\3\2\2\2\25\66")
        buf.write("\3\2\2\2\278\3\2\2\2\31:\3\2\2\2\33=\3\2\2\2\35A\3\2\2")
        buf.write("\2\37 \7f\2\2 \4\3\2\2\2!\"\7J\2\2\"\6\3\2\2\2#$\7N\2")
        buf.write("\2$\b\3\2\2\2%&\7H\2\2&\n\3\2\2\2\'-\5\r\7\2(-\5\17\b")
        buf.write("\2)-\5\21\t\2*-\5\23\n\2+-\5\25\13\2,\'\3\2\2\2,(\3\2")
        buf.write("\2\2,)\3\2\2\2,*\3\2\2\2,+\3\2\2\2-\f\3\2\2\2./\7-\2\2")
        buf.write("/\16\3\2\2\2\60\61\7/\2\2\61\20\3\2\2\2\62\63\7,\2\2\63")
        buf.write("\22\3\2\2\2\64\65\7\61\2\2\65\24\3\2\2\2\66\67\7z\2\2")
        buf.write("\67\26\3\2\2\289\7*\2\29\30\3\2\2\2:;\7+\2\2;\32\3\2\2")
        buf.write("\2<>\5\35\17\2=<\3\2\2\2>?\3\2\2\2?=\3\2\2\2?@\3\2\2\2")
        buf.write("@\34\3\2\2\2AB\4\62;\2B\36\3\2\2\2\5\2,?\2")
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
    OPEN_BRACKET = 11
    CLOSE_BRACKET = 12
    INTEGER_NUMBER = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'d'", "'H'", "'L'", "'F'", "'+'", "'-'", "'*'", "'/'", "'x'", 
            "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "FATE", "OPERATOR", "PLUS", "MINUS", "MULT", "DIV", "SEVERAL", 
            "OPEN_BRACKET", "CLOSE_BRACKET", "INTEGER_NUMBER" ]

    ruleNames = [ "T__0", "T__1", "T__2", "FATE", "OPERATOR", "PLUS", "MINUS", 
                  "MULT", "DIV", "SEVERAL", "OPEN_BRACKET", "CLOSE_BRACKET", 
                  "INTEGER_NUMBER", "DIGIT" ]

    grammarFileName = "dice.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


