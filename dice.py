#!/usr/bin/env python3

from antlr4 import tree
from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
from antlr4.error.ErrorListener import ErrorListener
from grammar.diceLexer import diceLexer
from grammar.diceParser import diceParser
from grammar.diceListener import diceListener

from random import randint
import warnings
import math
import sys

rand_fn = None

warnings.simplefilter('always')

MAX_EXPLOSION = 20
MAX_IMPLOSION = 20


class InvalidDiceRoll(Exception):
    pass


class GrammarParsingException(Exception):
    pass


class MyErrorListener(ErrorListener):
    def __init__(self):
        super(MyErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("syntaxError")
        raise InvalidDiceRoll

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex,
                        exact, ambigAlts, configs):
        print("reportAmbiguity")
        raise InvalidDiceRoll

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex,
                                    stopIndex, conflictingAlts, configs):
        print("reportAttemptingFullContext")
        raise InvalidDiceRoll

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        print("reportContextSensitivity")
        raise InvalidDiceRoll


def roll(s, override_rand=None, grammar_errors=True):
    global rand_fn

    if override_rand is not None:
        rand_fn = override_rand
    else:
        rand_fn = randint

    in_stream = InputStream(s)
    lexer = diceLexer(in_stream)

    lexer._listeners = [MyErrorListener()]

    stream = CommonTokenStream(lexer)
    parser = diceParser(stream)

    tree = parser.schema()
    printer = diceRollListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    if parser.getNumberOfSyntaxErrors() > 0:
        raise GrammarParsingException

    return printer.result


def getEmbeddedValues(ctx):
    vals = []
    for x in ctx.getChildren():
        if hasattr(x, "current_total"):
            # print(x.current_total)
            if isinstance(x.current_total, list):
                vals.append(x.current_total[0])
            else:
                vals.append(x.current_total)
        else:
            pass
    return vals


class diceRollListener(diceListener):
    def __init__(self):
        self.rolls = []
        self.result = 0

    def exitExactMatch(self, ctx):
        raise NotImplementedError

    def exitLessOrEqualTo(self, ctx):
        raise NotImplementedError

    def exitGreaterThanOrEqualTo(self, ctx):
        raise NotImplementedError

    def exitLessThan(self, ctx):
        raise NotImplementedError

    def exitGreaterThan(self, ctx):
        raise NotImplementedError

    def exitSequence(self, ctx):
        ctx.current_total = getEmbeddedValues(ctx)

    def exitDuplicate(self, ctx):
        raise NotImplementedError

    def enterAssignment(self, ctx):
        raise NotImplementedError

    def enterMacroFace(self, ctx):
        raise NotImplementedError

    def exitFaces(self, ctx):
        ctx.current_total = getEmbeddedValues(ctx)
        # for x in ctx.getChildren():
        #     print(type(x))

    def exitSchema(self, ctx):
        # todo - many
        self.result = getEmbeddedValues(ctx)
        if len(self.result) > 1:
            raise NotImplementedError
        else:
            self.result = self.result[0]
        # return self.result, self.rolls

    def exitBang(self, ctx):
        self.bangs = len([c for c in ctx.getText() if c == '!'])
        self.sucks = len([c for c in ctx.getText() if c == '~'])

    def exitForce(self, ctx):
        raise NotImplementedError

    def exitReroll(self, ctx):
        raise NotImplementedError

    def exitCondition(self, ctx):
        raise NotImplementedError

    def exitFateDie(self, ctx):
        self.current_face = "Fate"

    def exitSubset(self, ctx):
        raise NotImplementedError

    def exitVariable(self, ctx):
        raise NotImplementedError

    def enterDie_roll(self, ctx):
        self.current_face = None
        self.current_amount = None
        ctx.current_total = 0

    def exitSequence(self, ctx):
        ctx.current_total = getEmbeddedValues(ctx)


    def exitDie_roll(self, ctx):
        global rand_fn

        ctx.rolls = []
        ctx.current_total = 0

        if isinstance(self.current_face, int) and self.current_face < 1:
            raise InvalidDiceRoll

        if hasattr(self, "bangs") and self.bangs > 1:
            raise InvalidDiceRoll
        if hasattr(self, "sucks") and self.sucks > 1:
            raise InvalidDiceRoll
        if hasattr(self, "bangs") and self.bangs > 0 and \
                (not isinstance(self.current_face, str) and self.current_face < 2):
            raise InvalidDiceRoll
        if hasattr(self, "sucks") and self.sucks > 0 and \
                (not isinstance(self.current_face, str) and self.current_face < 2 ):
            raise InvalidDiceRoll

        if self.current_amount is None:
            # Case where we have d4 instead of 1d4
            self.current_amount = 1

        if self.current_face is None:
            # Just a value
            ctx.current_total = self.current_amount
            return

        if self.current_face == "Fate":
            low = -1
            high = 1
        else:
            low = 1
            high = self.current_face

        if hasattr(self, "bangs"):
            exploding = (self.bangs > 0 and self.bangs is not None)
        else:
            exploding = False

        if hasattr(self, "sucks"):
            imploding = (self.sucks > 0 and self.sucks is not None)
            if imploding and low >= 0:
                print("Cannot implode a roll which is positive")
                raise InvalidDiceRoll
        else:
            imploding = False

        warping = exploding or imploding

        approach_max_explosion = approach_max_implosion = 0
        rolled_dice = 0
        while approach_max_explosion < MAX_EXPLOSION and \
                approach_max_implosion < MAX_IMPLOSION:
            multi_roll = 0
            for _ in range(self.current_amount):

                r = rand_fn(low, high)

                ctx.rolls.append(r)
                multi_roll += r

            if (multi_roll == high*self.current_amount and exploding):
                approach_max_explosion += 1
                rolled_dice += multi_roll
            elif (multi_roll == low*self.current_amount and imploding):
                approach_max_implosion += 1
                rolled_dice += multi_roll
            else:
                rolled_dice += multi_roll
                ctx.current_total = rolled_dice
                break

        if approach_max_explosion >= MAX_EXPLOSION or \
                approach_max_implosion >= MAX_IMPLOSION:
            ctx.current_total = rolled_dice

        if False:
            print("Die Roll: ", ctx.current_total)

    def exitBubbleMulDiv(self, ctx):
        vals = getEmbeddedValues(ctx)
        ctx.current_total = vals[0]

    def exitBubbleSeveral(self, ctx):
        vals = getEmbeddedValues(ctx)
        ctx.current_total = vals[0]

    def exitBubblePow(self, ctx):
        vals = getEmbeddedValues(ctx)
        ctx.current_total = vals[0]

    def exitBubbleNeg(self, ctx):
        # print("BUBBLE NEG")
        vals = getEmbeddedValues(ctx)
        ctx.current_total = vals[0]

    def exitNoNegate(self, ctx):
        # print("No Negate")
        vals = getEmbeddedValues(ctx)
        ctx.current_total = vals[0]

    def exitPower(self, ctx):
        vals = getEmbeddedValues(ctx)
        ctx.current_total = math.pow(vals[0], vals[1])

    def exitNegate(self, ctx):
        # print("Negate")

        vals = getEmbeddedValues(ctx)
        ctx.current_total = -vals[0]

    def exitCount(self, ctx):
        raise NotImplementedError

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

    def exitSeveral(self, ctx):
        raise NotImplementedError

    def exitMul(self, ctx):
        vals = getEmbeddedValues(ctx)
        ctx.current_total = vals[0] * vals[1]

    def exitDivUp(self, ctx):
        vals = getEmbeddedValues(ctx)
        ctx.current_total = math.ceil(vals[0] / vals[1])

    def exitModulo(self, ctx):
        vals = getEmbeddedValues(ctx)
        ctx.current_total = vals[0] % vals[1]

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


if __name__ == "__main__":
    print(roll(sys.argv[1]))
