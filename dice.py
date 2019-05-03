from antlr4 import tree
from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
from grammar.diceLexer import diceLexer
from grammar.diceParser import diceParser
from grammar.diceListener import diceListener

from random import randint
import math

rand_fn = None


def roll(s, override_rand=None):
    global rand_fn

    if override_rand is not None:
        rand_fn = override_rand
    else:
        rand_fn = randint

    in_stream = InputStream(s)
    lexer = diceLexer(in_stream)
    stream = CommonTokenStream(lexer)
    parser = diceParser(stream)
    
    tree = parser.schema()
    printer = diceRollListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    return printer.result


def resolve_op_symbol(symbol):
    if symbol == "*":
        return "MUL"
    if symbol == "+":
        return "ADD"
    if symbol == "-":
        return "SUB"
    if symbol == "/":
        return "DIV_ROUND_DOWN"
    if symbol == "|":
        return "DIV_ROUND_UP"
    if symbol in ["x", "X"]:
        return "REPEAT"
    else:
        print("Unknown Arithmetic:", c.getText())

def do_operation(a, op, b):
    if op == "MUL":
        return a*b
    if op == "ADD":
        return a+b
    if op == "SUB":
        return a-b
    if op == "DIV_ROUND_DOWN":
        return a//b
    if op == "DIV_ROUND_UP":
        return math.ceil(a/b)
    if op == "REPEAT":
        print("Unsupported")
        raise Exception


class diceRollListener(diceListener):
    def __init__(self):
        self.rolls = []
        self.result = 0

    def enterSchema(self, ctx):
        # print("Schema", ctx.getText())
        pass
    
    def exitSchema(self, ctx):
        # print(self.result)
        return self.result, self.rolls


    def enterDie_roll(self, ctx):
        # print("enterDieRoll")
        self.current_face = 0
        self.current_amount = 0
        self.current_total = 0

    def exitDie_roll(self, ctx):
        global rand_fn

        if self.current_amount < 1: 
            self.current_amount = 1
        if self.current_face < 1:
            self.current_face = 1
            
        for _ in range(self.current_amount):
            r = rand_fn(1, self.current_face)
            self.rolls.append(r)
            self.current_total += r

        ctx.current_total = self.current_total
        self.roll_totals.append(self.current_total)


    def enterDice_roll(self, ctx):
        self.roll_totals = []
        
        self.values = []
        self.operation = None
        self.result = None


    def exitDice_roll(self, ctx):
        # print(ctx)
        # print(dir(ctx))

        for c in ctx.getChildren():
            if isinstance(c, tree.Tree.TerminalNode):
                # Operator
                self.operation = resolve_op_symbol(c.getText())                
            elif isinstance(c, diceParser.Die_rollContext):
                # Dice Roll Result
                self.values.append( c.current_total )
            elif isinstance(c, diceParser.Dice_rollContext):
                self.result = do_operation(self.values[1], self.operation, self.values[0])
            else:
                print("Unknown type: ", type(c))
                raise TypeException

        # print("Pass.", self.values, self.operation, self.result)

        if self.result is None:
            # Not operated on
            self.result = self.values[0]


    def enterFaces(self, ctx):
        self.current_face = int(ctx.getText())

    def enterAmount(self, ctx):
        self.current_amount = int(ctx.getText())

    def enterEveryRule(self, ctx):
        # print("rule - ", ctx.getText())
        pass