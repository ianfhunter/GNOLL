#!/usr/bin/env python3

from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
from antlr4.error.ErrorListener import ErrorListener

from grammar.diceLexer import diceLexer
from grammar.diceParser import diceParser
from grammar.diceListener import diceListener

from random import randint, choice
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

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex,
                                 prediction, configs):
        print("reportContextSensitivity")
        raise InvalidDiceRoll


def choose_item(items):
    return choice(items)


def roll(s, override_rand=None, grammar_errors=True):
    global rand_fn

    if override_rand is not None:
        rand_fn = override_rand
    else:
        rand_fn = choose_item

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


def bubbleImportantFields(ctx):
    for x in ctx.getChildren():
        if not hasattr(ctx, "dice_class") and hasattr(x, "dice_class"):
            ctx.dice_class = x.dice_class
        if not hasattr(ctx, "current_total") and hasattr(x, "current_total"):
            ctx.current_total = x.current_total


def getEmbeddedDiceRoll(ctx):
    die = None
    for x in ctx.getChildren():
        if hasattr(x, "dice_class"):
            die = x.dice_class

    return die


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

class Dice():
    def __init__(self, values, minmax=True, name="Anonymous"):
        if len(values) < 1:
            # Nothing to choose
            raise InvalidDiceRoll

        self.values = values
        self.name = name
        if minmax:
            self.lowest = self.values[0]
            self.highest = self.values[-1]

    def roll(self):
        global rand_fn
        return rand_fn(self.values)


class diceRollListener(diceListener):
    def __init__(self):
        self.rolls = []
        self.result = 0
        self.variable_table = {}

    def exitExactMatch(self, ctx):
        raise NotImplementedError

    def exitLessOrEqualTo(self, ctx):
        raise NotImplementedError

    def exitGreaterThanOrEqualTo(self, ctx):
        raise NotImplementedError

    def enterLessThan(self, ctx):
        raise NotImplementedError

    def exitLessThan(self, ctx):
        raise NotImplementedError

    def exitGreaterThan(self, ctx):
        raise NotImplementedError

    def exitSequence(self, ctx):
        ctx.current_total = getEmbeddedValues(ctx)

    def exitDuplicate(self, ctx):
        raise NotImplementedError

    def exitAssignment(self, ctx):

        for idx, c in enumerate(ctx.getChildren()):
            if '@' in c.getText():
                var = c.getText()[1:]
            try:
                die = getEmbeddedDiceRoll(c)
            except Exception:
                pass

        self.roll = die
        self.variable_table[var] = die
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
        if self.sucks > 1 or self.bangs > 1:
            raise NotImplementedError

    def exitForce(self, ctx):
        raise NotImplementedError

    def exitReroll(self, ctx):
        raise NotImplementedError

    def exitCondition(self, ctx):
        raise NotImplementedError

    def exitFateDie(self, ctx):
        ctx.dice_class = Dice(['-', '0', '+'], name="Fate")
        # raise NotImplementedError

    def exitSubset(self, ctx):
        raise NotImplementedError

    def exitVariable(self, ctx):
        self.variable_table[ctx.getText()[1:]] = "null"

    def enterDie_roll(self, ctx):
        self.current_face = None
        self.current_amount = None
        ctx.current_total = 0

    def exitDie_roll(self, ctx):
        global rand_fn

        d = getEmbeddedDiceRoll(ctx)

        for c in ctx.getChildren():
            if isinstance(c, diceParser.VariableContext):
                raise NotImplementedError

        ctx.rolls = []
        ctx.current_total = 0

        if isinstance(self.current_face, int) and self.current_face < 1:
            raise InvalidDiceRoll

        if hasattr(self, "bangs") and self.bangs > 1:
            raise InvalidDiceRoll
        if hasattr(self, "sucks") and self.sucks > 1:
            raise InvalidDiceRoll
        if hasattr(self, "bangs") and self.bangs > 0 and \
                (not isinstance(d.highest, str) and
                    d.highest < 2):
            raise InvalidDiceRoll
        if hasattr(self, "sucks") and self.sucks > 0 and \
                (not isinstance(d.lowest, str) and
                    d.lowest < 2):
            raise InvalidDiceRoll

        if self.current_amount is None:
            # Case where we have d4 instead of 1d4
            self.current_amount = 1

        if d is None:
            ctx.current_total = self.current_amount
            return

        if hasattr(self, "bangs"):
            exploding = (self.bangs > 0 and self.bangs is not None)
        else:
            exploding = False

        if hasattr(self, "sucks"):
            imploding = (self.sucks > 0 and self.sucks is not None)
            if imploding and type(d.lowest) != str and d.lowest >= 0:
                print("Cannot implode a roll which is positive")
                raise InvalidDiceRoll
        else:
            imploding = False

        # warping = exploding or imploding

        approach_max_explosion = approach_max_implosion = 0
        rolled_dice = 0


        multi_roll = []
        while approach_max_explosion < MAX_EXPLOSION and \
                approach_max_implosion < MAX_IMPLOSION:
            for _ in range(self.current_amount):

                r = d.roll()

                ctx.rolls.append(r)
                multi_roll.append(r)

            if (multi_roll[-1] == d.highest and exploding):
                approach_max_explosion += 1
                if type(multi_roll[-1]) not in [int, float]:
                    rolled_dice = "".join(multi_roll)
                else:
                    rolled_dice = sum(multi_roll)
            elif (multi_roll[-1] == d.lowest and imploding):
                approach_max_implosion += 1
                # SHould probably not be sum
                if type(multi_roll[-1]) not in [int, float]:
                    rolled_dice = "".join(multi_roll)
                else:
                    rolled_dice = sum(multi_roll)
            else:
                if type(multi_roll[-1]) not in [int, float]:
                    ctx.current_total = "".join(multi_roll)
                else:
                    rolled_dice = sum(multi_roll)
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
        if type(vals[0]) != type(vals[1]):
            raise NotImplementedError
        ctx.current_total = vals[0] + vals[1]

    def exitSub(self, ctx):
        vals = getEmbeddedValues(ctx)
        if type(vals[0]) is str or type(vals[1]) is str:
            raise NotImplementedError
        ctx.current_total = vals[0] - vals[1]

    def exitSeveral(self, ctx):
        raise NotImplementedError

    def exitMul(self, ctx):
        vals = getEmbeddedValues(ctx)
        if type(vals[0]) is str or type(vals[1]) is str:
            raise NotImplementedError
        ctx.current_total = vals[0] * vals[1]

    def exitDivUp(self, ctx):
        vals = getEmbeddedValues(ctx)
        if type(vals[0]) is str or type(vals[1]) is str:
            raise NotImplementedError
        ctx.current_total = math.ceil(vals[0] / vals[1])

    def exitModulo(self, ctx):
        vals = getEmbeddedValues(ctx)
        if type(vals[0]) is str or type(vals[1]) is str:
            raise NotImplementedError
        ctx.current_total = vals[0] % vals[1]

    def exitDivDown(self, ctx):
        vals = getEmbeddedValues(ctx)
        if type(vals[0]) is str or type(vals[1]) is str:
            raise NotImplementedError
        ctx.current_total = vals[0] // vals[1]

    def exitDice_roll(self, ctx):
        ctx.current_total = 0

        for c in ctx.getChildren():
            if isinstance(c, diceParser.Math_addsubContext):
                ctx.current_total = c.current_total
            else:
                print("Unknown type: ", type(c))

    def enterStandardFace(self, ctx):

        number = int(ctx.getText())

        self.current_face = number
        if(self.current_face < 0):
            print("Negative Dice Face.", file=sys.stderr)
            raise InvalidDiceRoll
        if(self.current_face < 0):
            print("No Dice Face.", file=sys.stderr)
            raise InvalidDiceRoll

        ctx.dice_class = Dice(list(range(1, number+1)))

    def enterAmount(self, ctx):
        self.current_amount = int(ctx.getText())
        if(self.current_amount < 0):
            print("Negative Amount of Dice.")
            raise InvalidDiceRoll

    def enterEveryRule(self, ctx, debug=False):
        # debug=True
        if debug:
            print(ctx.__class__, "\t=", ctx.getText())
            # print(list(ctx.getChildren()))

    def exitEveryRule(self, ctx):
        bubbleImportantFields(ctx)


if __name__ == "__main__":
    print("Roll Result:", roll(sys.argv[1]))
