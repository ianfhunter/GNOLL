from antlr4 import tree
from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
from antlr4.error import ErrorListener
from grammar.diceLexer import diceLexer
from grammar.diceParser import diceParser
from grammar.diceListener import diceListener

from random import randint
import math, sys

rand_fn = None

class InvalidDiceRoll(Exception):
    pass

class GrammarParsingException(Exception):
    pass


def roll(s, override_rand=None, grammar_errors=True):
    global rand_fn

    if override_rand is not None:
        rand_fn = override_rand
    else:
        rand_fn = randint

    in_stream = InputStream(s)
    lexer = diceLexer(in_stream)

    # if grammar_errors:
    #     cel = ErrorListener.ConsoleErrorListener
    #     if cel not in lexer._listeners:
    #         lexer.addErrorListener(cel)
    # else:
    #     lexer.removeErrorListener(ErrorListener.ConsoleErrorListener);

    stream = CommonTokenStream(lexer)
    parser = diceParser(stream)
    
    tree = parser.schema()
    printer = diceRollListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    if parser.getNumberOfSyntaxErrors() > 0:
        raise GrammarParsingException

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


def getEmbeddedValues(ctx):
    vals = []
    for x in ctx.getChildren():
        if hasattr(x, "current_total"):
            print(x.current_total)
            if isinstance(x.current_total, list): 
                vals.append(x.current_total[0])
            else:
                vals.append(x.current_total)
        else:
            print(type(x))
            print(x.current_total)
    return vals

class diceRollListener(diceListener):
    def __init__(self):
        self.rolls = []
        self.result = 0

    def exitSequence(self, ctx):
        ctx.current_total = getEmbeddedValues(ctx)
    
    def exitDuplicate(self, ctx):
        raise NotImplementedError

    def exitFaces(self, ctx):
    
        for x in ctx.getChildren():
            print(type(x))

    def exitSchema(self, ctx):
        #todo - many
        self.result = getEmbeddedValues(ctx)
        if len(self.result) > 1:
            raise NotImplementedError
        else:
            self.result = self.result[0]
        # return self.result, self.rolls



    def exitBang(self, ctx):
        raise NotImplementedError

    def exitForce(self, ctx):
        raise NotImplementedError

    def exitReroll(self, ctx):
        raise NotImplementedError

    def exitSubset(self, ctx):
        raise NotImplementedError
        
    def enterDie_roll(self, ctx):
        self.current_face = None
        self.current_amount = None
        self.current_total = 0
        pass


    def exitSequence(self, ctx):
        ctx.current_total = getEmbeddedValues(ctx)

    def exitDie_roll(self, ctx):
        global rand_fn

        ctx.rolls = []
        ctx.current_total = 0

        if self.current_amount is None: 
            # Case where we have d4 instead of 1d4
            self.current_amount = 1
            
        for _ in range(self.current_amount):
            if self.current_face is None:
                # Case of just Value
                r = 1
            elif self.current_face == 0:
                r = 0
            else:
                r = rand_fn(1, self.current_face)

            ctx.rolls.append(r)
            ctx.current_total += r

        if False:
            print("Die Roll: ", ctx.current_total)



    def exitMath(self, ctx):
        vals = getEmbeddedValues(ctx)
        ctx.current_total = vals[0] 

    def exitBubbleMulDiv(self, ctx):
        vals = getEmbeddedValues(ctx)
        ctx.current_total = vals[0] 

    def exitBubblePow(self, ctx):
        vals = getEmbeddedValues(ctx)
        if len(vals) > 1:
            ctx.current_total = vals[0] ^ vals[1]
        else:
            ctx.current_total = vals[0] 

    def exitBubbleNeg(self, ctx):
        # print("BUBBLE NEG")
        vals = getEmbeddedValues(ctx)
        ctx.current_total = vals[0] 

    def exitNoNegate(self, ctx):
        # print("No Negate")
        vals = getEmbeddedValues(ctx)
        ctx.current_total = vals[0] 

    def exitNegate(self, ctx):
        # print("Negate")

        vals = getEmbeddedValues(ctx)
        ctx.current_total = -vals[0] 

    def exitCustomFace(self, ctx):
        raise NotImplementedError

    def exitValue(self, ctx):
        vals = getEmbeddedValues(ctx)
        ctx.current_total = vals[0] 

    def exitBrackets(self, ctx):
        vals = getEmbeddedValues(ctx)
        ctx.current_total = vals[0] 

    def exitAdd(self, ctx):  
        vals = getEmbeddedValues(ctx)
        ctx.current_total = vals[0] + vals[1]

    def exitSub(self, ctx):        
        vals = getEmbeddedValues(ctx)
        ctx.current_total = vals[0] - vals[1]

    def exitMul(self, ctx):        
        vals = getEmbeddedValues(ctx)
        ctx.current_total = vals[0] * vals[1]

    def exitDivUp(self, ctx):        
        vals = getEmbeddedValues(ctx)
        ctx.current_total = math.ceil(vals[0] / vals[1])

    def exitDivDown(self, ctx):        
        vals = getEmbeddedValues(ctx)
        ctx.current_total = vals[0] // vals[1]


    def exitDice_roll(self, ctx):
        ctx.current_total = 0

        for c in ctx.getChildren():
            if isinstance(c, diceParser.Math_addsubContext):
                ctx.current_total = c.current_total
            else:
                print("Unknown type: ", type(c))


    def enterStandardFace(self, ctx):
        self.current_face = int(ctx.getText())
        if(self.current_face < 0):
            print("Negative Dice Face.", file=sys.stderr)
            raise InvalidDiceRoll
        if(self.current_face < 0):
            print("No Dice Face.", file=sys.stderr)
            raise InvalidDiceRoll

    def enterAmount(self, ctx):
        self.current_amount = int(ctx.getText())
        if(self.current_amount < 0):
            print("Negative Amount of Dice.")
            raise InvalidDiceRoll

    def enterEveryRule(self, ctx):
        pass