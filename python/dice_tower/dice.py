#!/usr/bin/env python3

from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Trees import Trees

from dice_tower.grammar.diceLexer import diceLexer
from dice_tower.grammar.diceParser import diceParser
from dice_tower.grammar.diceListener import diceListener

from random import choice
import warnings
import math
import sys
import os

rand_fn = None
log = None

warnings.simplefilter('always')

MAX_EXPLOSION = 20
MAX_IMPLOSION = 20
REROLL_LIMIT = 20


class Verbosity():

    SILENT = 0
    ERROR = 1
    WARN = 2
    INFO = 3
    DEBUG = 4

    def __init__(self, verbosity_level):
        self.level = verbosity_level

    def eprint(self, *args):
        # error
        if self.level >= self.ERROR:
            print(*args)

    def wprint(self, *args):
        # warn
        if self.level >= self.WARN:
            print(*args)

    def iprint(self, *args):
        # info
        if self.level >= self.INFO:
            print(*args)

    def dprint(self, *args):
        # Debug
        if self.level >= self.DEBUG:
            print(*args)


class InvalidDiceRoll(Exception):
    pass


class GrammarParsingException(Exception):
    pass


class MyErrorListener(ErrorListener):
    def __init__(self):
        super(MyErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        log.eprint("syntaxError")
        raise InvalidDiceRoll

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex,
                        exact, ambigAlts, configs):
        log.wprint("reportAmbiguity")
        raise InvalidDiceRoll

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex,
                                    stopIndex, conflictingAlts, configs):
        log.wprint("reportAttemptingFullContext")
        # raise InvalidDiceRoll

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex,
                                 prediction, configs):
        log.eprint("reportContextSensitivity")
        raise InvalidDiceRoll


def choose_item(items):
    return choice(items)


def predefined_macros():
    preloaded_var_table = {}


    fp = os.path.dirname(os.path.realpath(__file__))
    f = open(os.path.join(fp, "links/macros.dice"))
    for x in f:
        x = x.rstrip()
        if "//" in x or x.isspace():
            continue
        r = roll(x, load_predefines=False,
                 __loading_macros=True, verbosity="null")
        nvt = r[1]
        preloaded_var_table.update(nvt)
    f.close()

    return preloaded_var_table


def roll(s, override_rand=None, grammar_errors=True, debug=False,
         verbosity="INFO", load_predefines=True, __loading_macros=False):
    global rand_fn
    global log


    log = Verbosity(Verbosity.ERROR)
    if not __loading_macros:
        if override_rand is not None:
            rand_fn = override_rand
        else:
            rand_fn = choose_item

    verbosity.strip()

    if verbosity != "null":
        if verbosity == "SILENT":
            log = Verbosity(Verbosity.SILENT)
        elif verbosity == "ERROR":
            log = Verbosity(Verbosity.ERROR)
        elif verbosity == "WARN":
            log = Verbosity(Verbosity.WARN)
        elif verbosity == "INFO":
            log = Verbosity(Verbosity.INFO)
        elif verbosity == "DEBUG":
            log = Verbosity(Verbosity.DEBUG)
        else:
            print("No Verbosity level named: \""+verbosity+"\"")
            raise ValueError

    if load_predefines:  # and False:
        vt = predefined_macros()
    else:
        vt = {}

    in_stream = InputStream(s)
    lexer = diceLexer(in_stream)

    lexer._listeners = [MyErrorListener()]

    stream = CommonTokenStream(lexer)
    parser = diceParser(stream)
    parser.addErrorListener(MyErrorListener())

    tree = parser.schema()

    log.dprint("\nParsed Pattern:", Trees.toStringTree(
        tree, None, parser), "\n")

    printer = diceRollListener(vtable=vt)

    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    if parser.getNumberOfSyntaxErrors() > 0:

        print("Syntax Errors Observed: Original String: ", s)
        print("\nParsed Pattern:",
              Trees.toStringTree(tree, None, parser), "\n")

        raise GrammarParsingException

    if __loading_macros:
        return printer.result, printer.variable_table
    else:
        return printer.result


def bubbleImportantFields(ctx):
    # Children give their attributes to their parents
    for x in ctx.getChildren():
        if not hasattr(ctx, "dice_class") and hasattr(x, "dice_class"):
            ctx.dice_class = x.dice_class
        if not hasattr(ctx, "current_total") and hasattr(x, "current_total"):
            ctx.current_total = x.current_total


def getEmbeddedDiceRoll(ctx):
    die = []
    for x in ctx.getChildren():
        if hasattr(x, "dice_class"):
            die.append(x.dice_class)

    if len(die) > 1:
        return die
    elif len(die) == 1:
        return die[0]
    else:
        return None


def condition_met(values, condition):
    if condition is None:
        return True

    if condition == "GREATER":
        return values[0] > values[1]
    elif condition == "GREATER_EQUAL":
        return values[0] >= values[1]
    elif condition == "LESSER":
        return values[0] < values[1]
    elif condition == "LESSER_EQUAL":
        return values[0] <= values[1]
    elif condition == "EQUAL":
        return values[0] == values[1]
    else:
        log.eprint("Condition not recognized:", condition)
        raise ValueError()


def getEmbeddedValues(ctx):
    vals = []
    for x in ctx.getChildren():
        if hasattr(x, "current_total"):
            if x.current_total == "null":
                continue
            if isinstance(x.current_total, list):
                if len(x.current_total) == 1:
                    vals.append(x.current_total[0])
                else:
                    vals.extend(x.current_total)
            else:
                vals.append(x.current_total)
        else:
            pass
    if len(vals) == 1:
        return vals[0]
    return vals


class Dice():
    def __init__(self, values, minmax=True, name="Anonymous"):
        if len(values) < 1:
            # Nothing to choose
            raise InvalidDiceRoll

        self.values = values
        self.name = name
        self.roll_record = []
        if minmax:
            self.lowest = self.values[0]
            self.highest = self.values[-1]

        self.type = "Numeric"
        for x in values:
            if type(x) == str:
                self.type = "Alphabetic"

    def roll(self, save=True):
        global rand_fn
        this_roll = rand_fn(self.values)
        if save:
            self.roll_record.append(this_roll)
        return this_roll

    def reroll(self, replace=False, distinct=False):
        """
            Rolls more dice and appends to the dice already rolled
            unless "replace" is True.
            "distinct" will ensure the rolls are not saved inside
            the dice object
        """
        already_rolled = len(self.roll_record)
        assert(already_rolled > 0)

        if replace:
            self.roll_record = []

        rr = []
        for x in range(already_rolled):
            rr.append(self.roll(save=not distinct))

        return rr


class diceRollListener(diceListener):
    def __init__(self, vtable={}):
        self.rolls = []
        self.result = 0
        self.variable_table = vtable
        if vtable != {}:
            log.iprint("Loaded Macros:", vtable)

    def exitExactMatch(self, ctx):
        self.check = "EQUAL"
        ctx.current_total = int(ctx.getText().strip("#").strip("="))

    def exitLessOrEqualTo(self, ctx):
        self.check = "LESSER_EQUAL"
        ctx.current_total = int(ctx.getText().strip("<").strip("="))

    def exitGreaterOrEqualTo(self, ctx):
        self.check = "GREATER_EQUAL"
        ctx.current_total = int(ctx.getText().strip(">").strip("="))

    def exitLessThan(self, ctx):
        self.check = "LESSER"
        ctx.current_total = int(ctx.getText().strip("<"))

    def exitGreaterThan(self, ctx):
        self.check = "GREATER"
        ctx.current_total = int(ctx.getText().strip(">"))

    def exitAssignment(self, ctx):
        for idx, c in enumerate(ctx.getChildren()):
            if '#' in c.getText():
                var = c.getText()[1:]
            try:
                die = getEmbeddedDiceRoll(c)
            except Exception:
                pass

        # self.roll = die
        self.variable_table[var] = die
        ctx.current_total = "null"

    def exitMultiItem(self, ctx):
        ctx.current_total = getEmbeddedValues(ctx)

    def exitSchema(self, ctx):
        self.result = getEmbeddedValues(ctx)

    def exitBang(self, ctx):
        self.bangs = len([c for c in ctx.getText() if c == '!'])
        self.sucks = len([c for c in ctx.getText() if c == '~'])
        if self.sucks > 1 or self.bangs > 1:
            raise NotImplementedError

    def exitForce(self, ctx):
        raise NotImplementedError

    def exitReroll(self, ctx):
        t = ctx.getText()
        if "rr" in t:
            self.rr = REROLL_LIMIT  # Keep rerolling forever
        elif "r" in t:
            tok = t.split("r")
            try:
                times = int(tok[-1])
            except Exception:
                times = 1

            self.rr = times  # Reroll Once

    def enterTryAgain(self, ctx):
        self.check = None

    def exitTryAgain(self, ctx):
        a = getEmbeddedValues(ctx)
        d = getEmbeddedDiceRoll(ctx)

        log.dprint("Original Val:", a)

        rerolls = 0

        if not condition_met(a, self.check):
            for x in range(self.rr):
                rerolls += 1
                log.iprint("Rerolling..")
                rolled = d.reroll(replace=True)

                if d.type == "Alphabetic":
                    rolled_dice = "".join(rolled)
                else:
                    rolled_dice = sum(rolled)

                log.iprint(rolled_dice, "replaces", a[0])

                a[0] = rolled_dice
                if condition_met(a, self.check):
                    break

        ctx.current_total = a[0]

        if REROLL_LIMIT >= rerolls and not condition_met(a, self.check):
            log.wprint("Maximum Reroll limit reached.")

    def exitCondition(self, ctx):
        raise NotImplementedError

    def exitFateDie(self, ctx):
        ctx.dice_class = Dice(['-', '0', '+'], name="Fate")
        # raise NotImplementedError

    def exitDoSubset(self, ctx):
        b = getEmbeddedDiceRoll(ctx)
        c = ctx.getText()
        dropLow = False
        if "kl" in c:
            dropLow = True
            v = c.split("kl")[-1]
            amount = int(v if v != "" else 1)
        elif "kh" in c:
            v = c.split("kh")[-1]
            amount = int(v if v != "" else 1)
        else:
            log.iprint("Only rolegate notation supported")
            raise NotImplementedError

        for x in b.roll_record:
            if isinstance(x, str):
                raise NotImplementedError

        if amount > len(b.roll_record):
            log.eprint("Err: Trying to drop", amount,
                       "from", len(b.roll_record))
            raise InvalidDiceRoll
        if amount == len(b.roll_record):
            log.iprint("No need to drop")
            return

        amount = len(b.roll_record) - amount

        if dropLow:
            log.iprint("Dropping Low Values")
            ctx.current_total = sorted(b.roll_record)[:-amount]
        else:
            log.iprint("Dropping High Values")
            ctx.current_total = sorted(b.roll_record)[amount:]

        if len(ctx.current_total) > 1:
            if b.type == "Alphabetic":
                ctx.current_total = "".join(ctx.current_total)
            else:
                ctx.current_total = sum(ctx.current_total)

    def exitAccess_variable(self, ctx):
        ctx.saved_var = self.variable_table[ctx.getText()[1:]]

    def enterDie_roll(self, ctx):
        self.current_face = None
        self.current_amount = None
        ctx.current_total = 0

    def exitDie_roll(self, ctx):
        global rand_fn

        d = getEmbeddedDiceRoll(ctx)

        for c in ctx.getChildren():
            if isinstance(c, diceParser.Access_variableContext):
                d = c.saved_var

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
                    d.lowest > -1):  # TODO: Better conditions can be made
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
                if d.type == "Alphabetic":
                    rolled_dice = "".join(multi_roll)
                else:
                    rolled_dice = sum(multi_roll)
            elif (multi_roll[-1] == d.lowest and imploding):
                approach_max_implosion += 1
                # SHould probably not be sum
                if d.type == "Alphabetic":
                    rolled_dice = "".join(multi_roll)
                else:
                    rolled_dice = sum(multi_roll)
            else:
                if d.type == "Alphabetic":
                    ctx.current_total = "".join(multi_roll)
                else:
                    rolled_dice = sum(multi_roll)
                    ctx.current_total = rolled_dice
                break

        if approach_max_explosion >= MAX_EXPLOSION or \
                approach_max_implosion >= MAX_IMPLOSION:
            log.wprint("Maximum Implosion/Explosion reached.")
            ctx.current_total = rolled_dice

        if False:
            print("Die Roll: ", ctx.current_total)

    def exitBubbleMulDiv(self, ctx):
        vals = getEmbeddedValues(ctx)
        ctx.current_total = vals

    def exitBubbleSeveral(self, ctx):
        vals = getEmbeddedValues(ctx)
        ctx.current_total = vals

    def exitBubblePow(self, ctx):
        vals = getEmbeddedValues(ctx)
        ctx.current_total = vals

    def exitBubbleNeg(self, ctx):
        # print("BUBBLE NEG")
        vals = getEmbeddedValues(ctx)
        ctx.current_total = vals

    def exitNoNegate(self, ctx):
        # print("No Negate")
        vals = getEmbeddedValues(ctx)
        ctx.current_total = vals

    def exitPower(self, ctx):
        vals = getEmbeddedValues(ctx)
        ctx.current_total = math.pow(vals[0], vals[1])

    def exitNegate(self, ctx):
        vals = getEmbeddedValues(ctx)
        ctx.current_total = -vals

    def exitCount(self, ctx):
        raise NotImplementedError

    def exitCountSuccess(self, ctx):
        raise NotImplementedError

    def exitNSequence(self, ctx):
        ctx.current_total = getEmbeddedValues(ctx)

    def exitNumeric_item(self, ctx):
        if hasattr(ctx, "current_total"):
            ctx.current_total.append(ctx.getText())
        else:
            ctx.current_total = ctx.getText()

    def exitSeq_item(self, ctx):
        raise NotImplementedError

    def exitCustomFace(self, ctx):
        values = getEmbeddedValues(ctx)
        try:
            v = [int(x) for x in values]
            values = v
        except ValueError:
            pass
        ctx.dice_class = Dice(values)

    def exitValue(self, ctx):
        vals = getEmbeddedValues(ctx)
        ctx.current_total = vals

    def exitBrackets(self, ctx):
        vals = getEmbeddedValues(ctx)
        ctx.current_total = vals

    def exitAdd(self, ctx):
        vals = getEmbeddedValues(ctx)
        if not isinstance(vals[0], type(vals[1])):
            raise InvalidDiceRoll
        ctx.current_total = vals[0] + vals[1]

        ds = getEmbeddedDiceRoll(ctx)
        ctx.dice_class = ds

    def exitSub(self, ctx):
        vals = getEmbeddedValues(ctx)
        if isinstance(vals[0], str) or isinstance(vals[1], str):
            raise InvalidDiceRoll
        ctx.current_total = vals[0] - vals[1]

    def exitSev(self, ctx):
        d = getEmbeddedDiceRoll(ctx)
        bvals = getEmbeddedValues(ctx)

        if type(d) is list and len(d) > 1:
            log.iprint("Repeating Dice arithmetic is not supported yet")
            raise NotImplementedError

        last_dice_roll = bvals[0]
        times_to_repeat = bvals[1] - 1
        if(times_to_repeat < 0):
            raise InvalidDiceRoll

        v = [last_dice_roll]
        log.iprint("Repeat")
        for x in range(times_to_repeat):
            v.extend(d.reroll(distinct=True))
        ctx.current_total = v

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

    def exitDoBang(self, ctx):
        raise NotImplementedError

    def exitDice_roll(self, ctx):
        ctx.current_total = 0

        for c in ctx.getChildren():
            # Needed?
            if hasattr(c, "current_total"):
                ctx.current_total = c.current_total

    def enterStandardFace(self, ctx):

        number = int(ctx.getText())

        self.current_face = number
        if(self.current_face < 0):
            log.eprint("Negative Dice Face.")
            raise InvalidDiceRoll
        if(self.current_face < 0):
            log.eprint("No Dice Face.")
            raise InvalidDiceRoll

        ctx.dice_class = Dice(list(range(1, number+1)))

    def enterAmount(self, ctx):
        self.current_amount = int(ctx.getText())
        if(self.current_amount < 0):
            log.eprint("Negative Amount of Dice.")
            raise InvalidDiceRoll

    def enterEveryRule(self, ctx, ):
        log.dprint(ctx.__class__, "\tText=", ctx.getText())

    def exitEveryRule(self, ctx):
        bubbleImportantFields(ctx)
        if hasattr(ctx, "current_total"):
            ct = ctx.current_total
        else:
            ct = "None"
        log.dprint(ctx.__class__, "\t\tValue=", ct)


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-D":
        print("Debug Enabled")
        print("Roll Result:", roll(sys.argv[1], verbosity="DEBUG"))
    elif len(sys.argv) > 2 and sys.argv[2] == "-Q":
        print("Roll Result:", roll(sys.argv[1], verbosity="SILENT"))
    else:
        print("Roll Result:", roll(sys.argv[1], verbosity="INFO"))
