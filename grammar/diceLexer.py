# Generated from dice.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("T\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5")
        buf.write("\6\65\n\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3")
        buf.write("\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\6\20J\n\20\r\20")
        buf.write("\16\20K\3\21\3\21\3\22\6\22Q\n\22\r\22\16\22R\2\2\23\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\2#\2\3\2\3\4\2\13\13\"\"\2Y\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\3%\3\2\2\2\5\'\3\2\2\2\7)\3\2")
        buf.write("\2\2\t+\3\2\2\2\13\64\3\2\2\2\r\66\3\2\2\2\178\3\2\2\2")
        buf.write("\21:\3\2\2\2\23<\3\2\2\2\25>\3\2\2\2\27@\3\2\2\2\31B\3")
        buf.write("\2\2\2\33D\3\2\2\2\35F\3\2\2\2\37I\3\2\2\2!M\3\2\2\2#")
        buf.write("P\3\2\2\2%&\7f\2\2&\4\3\2\2\2\'(\7J\2\2(\6\3\2\2\2)*\7")
        buf.write("N\2\2*\b\3\2\2\2+,\7H\2\2,\n\3\2\2\2-\65\5\17\b\2.\65")
        buf.write("\5\23\n\2/\65\5\25\13\2\60\65\5\27\f\2\61\65\5\r\7\2\62")
        buf.write("\65\5\21\t\2\63\65\5\31\r\2\64-\3\2\2\2\64.\3\2\2\2\64")
        buf.write("/\3\2\2\2\64\60\3\2\2\2\64\61\3\2\2\2\64\62\3\2\2\2\64")
        buf.write("\63\3\2\2\2\65\f\3\2\2\2\66\67\7-\2\2\67\16\3\2\2\289")
        buf.write("\7`\2\29\20\3\2\2\2:;\7/\2\2;\22\3\2\2\2<=\7,\2\2=\24")
        buf.write("\3\2\2\2>?\7\61\2\2?\26\3\2\2\2@A\7~\2\2A\30\3\2\2\2B")
        buf.write("C\7z\2\2C\32\3\2\2\2DE\7*\2\2E\34\3\2\2\2FG\7+\2\2G\36")
        buf.write("\3\2\2\2HJ\5!\21\2IH\3\2\2\2JK\3\2\2\2KI\3\2\2\2KL\3\2")
        buf.write("\2\2L \3\2\2\2MN\4\62;\2N\"\3\2\2\2OQ\t\2\2\2PO\3\2\2")
        buf.write("\2QR\3\2\2\2RP\3\2\2\2RS\3\2\2\2S$\3\2\2\2\6\2\64KR\2")
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
    POWER = 7
    MINUS = 8
    MULT = 9
    DIV = 10
    DIV_RUP = 11
    SEVERAL = 12
    OPEN_BRACKET = 13
    CLOSE_BRACKET = 14
    INTEGER_NUMBER = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'d'", "'H'", "'L'", "'F'", "'+'", "'^'", "'-'", "'*'", "'/'", 
            "'|'", "'x'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "FATE", "OPERATOR", "PLUS", "POWER", "MINUS", "MULT", "DIV", 
            "DIV_RUP", "SEVERAL", "OPEN_BRACKET", "CLOSE_BRACKET", "INTEGER_NUMBER" ]

    ruleNames = [ "T__0", "T__1", "T__2", "FATE", "OPERATOR", "PLUS", "POWER", 
                  "MINUS", "MULT", "DIV", "DIV_RUP", "SEVERAL", "OPEN_BRACKET", 
                  "CLOSE_BRACKET", "INTEGER_NUMBER", "DIGIT", "WSPACE" ]

    grammarFileName = "dice.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


