from antlr4 import *
from grammar.diceLexer import diceLexer
from grammar.diceParser import diceParser
from grammar.diceListener import diceListener
from random import randint

def roll(s):
    in_stream = InputStream(s)
    lexer = diceLexer(in_stream)
    stream = CommonTokenStream(lexer)
    parser = diceParser(stream)
    
    tree = parser.schema()
    printer = diceRollListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    return printer.rolls


class diceRollListener(diceListener):
    def __init__(self):
        self.rolls = []

    def enterSchema(self, ctx):
        # print("Schema", ctx.getText())
        pass
    
    def exitSchema(self, ctx):
        return self.rolls

    def enterDice_roll(self, ctx):
        pass
        # print("enterDiceRoll")

    def enterDie_roll(self, ctx):
        # print("enterDieRoll")
        self.current_face = 0
        self.current_amount = 0

    def exitDice_roll(self, ctx):
        # print("exitDieRoll")

        for n in range(self.current_amount):
            r = randint(1, self.current_face)
            self.rolls.append(r)

        # print("Rolls:", self.rolls)

    def enterFaces(self, ctx):
        self.current_face = int(ctx.getText())

    def enterAmount(self, ctx):
        self.current_amount = int(ctx.getText())

    def enterEveryRule(self, ctx):
        # print("rule - ", ctx.getText())
        pass