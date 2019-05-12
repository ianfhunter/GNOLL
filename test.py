#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import unittest
import xmlrunner

from dice import roll, GrammarParsingException, InvalidDiceRoll

from contextlib import contextmanager
import os
import sys


def not_random_lowest(randint_start=0, randint_end=99):
    return randint_start


def not_random_highest(randint_start=0, randint_end=99):
    return randint_end


def graph(values, name):
    values = np.array(values).flatten()

    # the histogram of the data
    # print(np.unique(values))
    # plt.plot(xdata=np.unique(values), ydata=values)
    plt.hist(values)
    # print(np.std(values))

    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.title('Histogram of Dice Roll')
    plt.savefig(name+'.png')


def testHigh(s):
    return roll(s, override_rand=not_random_highest)


def testLow(s):
    return roll(s, override_rand=not_random_lowest)


def spread(s, fail=False):

    v = []
    v.append(testLow(s))
    v.append(testHigh(s))
    vs = np.arange(v[0], v[1]+1)
    return vs


def display(s):
    v = []
    for n in range(10000):
        v.append(roll(s))

    if False:
        graph(v, s)
    return v


def check_values(roll_text, lowest=0, highest=0, debug=False):

    data = spread(roll_text)

    expected = np.arange(lowest, highest+1)
    data = np.unique(np.array(data).flatten())
    if debug:
        print(data, expected)

    return np.array_equal(data, expected), data, expected, roll_text


@contextmanager
def suppress_prints():
    with open(os.devnull, "w") as devnull:
        old_stderr = sys.stderr
        old_stdout = sys.stdout
        sys.stderr = devnull
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stderr = old_stderr
            sys.stdout = old_stdout


class TestSuite(unittest.TestCase):

    def setup(self):
        np.random.seed(1)

    def tearDown(self):
        pass

    def assertTrue(self, fn, *args, **kwargs):
        # Override to provide error info upon failure
        try:
            cond, a, b, s = fn(*args, **kwargs)
            super(TestSuite, self).assertTrue(cond)
        except AssertionError:
            print("✗")
            print("Fail ["+s+"] - ", a, " did not equal expected value: ", b)
            raise AssertionError
        except NotImplementedError:
            print(u'\u231B', end="")
            cond = False

        if cond:
            print("✓", end="")

    def assertRaises(self, fn, *args, **kwargs):
        # override to reduce print noise
        cond = True
        with suppress_prints():
            try:
                super(TestSuite, self).assertRaises(fn, *args, kwargs)
            except NotImplementedError:
                print(u'\u231B', end="")
                cond = False

        if cond:
            print("✓", end="")

    def addFailure(self, test, err):
        # here you can do what you want to do when a test case fails
        print('\n\n\ntest failed!')
        super(TestSuite, self).addFailure(test, err)

    def test_single_dice(self):
        print("\n== Single Dice ==")
        self.assertTrue(check_values, "d4", lowest=1, highest=4)
        self.assertTrue(check_values, "1d4", lowest=1, highest=4)
        self.assertTrue(check_values, "1d6", lowest=1, highest=6)
        self.assertTrue(check_values, "1d8", lowest=1, highest=8)
        self.assertTrue(check_values, "1d10", lowest=1, highest=10)
        self.assertTrue(check_values, "1d12", lowest=1, highest=12)
        self.assertTrue(check_values, "1d20", lowest=1, highest=20)
        self.assertTrue(check_values, "1d100", lowest=1, highest=100)
        self.assertTrue(check_values, " 1d100 ", lowest=1, highest=100)

    def test_multiple_dice(self):
        print("\n== Multiple Dice ==")
        self.assertTrue(check_values, "d4", lowest=1, highest=4)
        self.assertTrue(check_values, "2d4", lowest=2, highest=8)
        self.assertTrue(check_values, "4d4", lowest=4, highest=16)
        self.assertTrue(check_values, "5d4", lowest=5, highest=20)

    def test_questionable_input(self):
        print("\n== Odd Cases ==")
        self.assertTrue(check_values, "0", lowest=0, highest=0)
        self.assertRaises(InvalidDiceRoll, check_values,
                          "0d0", lowest=0, highest=0)
        self.assertRaises(InvalidDiceRoll, check_values,
                          "-1d0", lowest=0, highest=0)
        self.assertTrue(check_values, "1-d1", lowest=0, highest=0)
        self.assertTrue(check_values, "1d1", lowest=1, highest=1)

        self.assertRaises(GrammarParsingException,
                          check_values, "0d", lowest=1, highest=4)
        self.assertRaises(InvalidDiceRoll, check_values,
                          "1d-1", lowest=0, highest=0)
        self.assertRaises(GrammarParsingException,
                          check_values, "d", lowest=0, highest=0)

    def test_rolls_with_arithmetic(self):
        print("\n== Arithmetic ==")
        self.assertTrue(check_values, "d4+d4", lowest=2, highest=8)
        # Doesn't quite work as face min != min result
        self.assertTrue(check_values, "d4+-d4", lowest=0, highest=0)
        self.assertTrue(check_values, "1d4+1d6", lowest=2, highest=10)
        self.assertTrue(check_values, "2d4+1d6", lowest=3, highest=14)
        self.assertTrue(check_values, "1d4+2", lowest=3, highest=6)
        self.assertTrue(check_values, "1d4-2", lowest=-1, highest=2)
        self.assertTrue(check_values, "1d4*2", lowest=2, highest=8)
        self.assertTrue(check_values, "1d4/2", lowest=0, highest=2)
        self.assertTrue(check_values, "1d4|2", lowest=1, highest=2)
        self.assertTrue(check_values, "1d4 + 1d6", lowest=2, highest=10)
        self.assertTrue(check_values, "  1d4 + 1d6 ", lowest=2, highest=10)
        self.assertTrue(check_values, "1d4+-1", lowest=0, highest=3)
        self.assertTrue(check_values, "1d4+-2", lowest=-1, highest=2)
        self.assertTrue(check_values, "1d4+----2", lowest=3, highest=6)
        self.assertTrue(check_values, "1d4----2", lowest=3, highest=6)
        self.assertTrue(check_values, "1d3+1d6+1d20", lowest=3, highest=29)
        self.assertTrue(check_values, "1d3+1d6 + 1d20", lowest=3, highest=29)
        self.assertTrue(check_values, "1+1", lowest=2, highest=2)
        self.assertTrue(check_values, "1+(1)", lowest=2, highest=2)
        self.assertTrue(check_values, "1d4-(2)", lowest=-1, highest=2)
        self.assertTrue(check_values, " ( 1d4 + 1d10 ) * 2",
                        lowest=4, highest=28)
        self.assertTrue(check_values, "d4^d4", lowest=1, highest=256)
        self.assertTrue(check_values, "d20%2", lowest=1, highest=0)

    def test_roll_sequences(self):
        print("\n== Sequences ==")
        self.assertTrue(check_values, "d4,d4", lowest=1, highest=4)
        self.assertRaises(GrammarParsingException, check_values,
                          "(d4,d4)", lowest=1, highest=4)
        self.assertTrue(check_values, "d4,d4,d4,d4,d4,d4", lowest=1, highest=4)
        self.assertTrue(check_values, "d4@2", lowest=1, highest=4)
        self.assertTrue(check_values, "(1d4+1d10)@2", lowest=2, highest=14)

    def test_conditions(self):
        self.assertTrue(check_values, "1d4#4r", lowest=1,
                        highest=4)  # Hard to tell if valid
        self.assertTrue(check_values, "1d4>3r", lowest=1,
                        highest=4)  # Hard to tell if valid
        self.assertTrue(check_values, "1d4<3r", lowest=1,
                        highest=4)  # Hard to tell if valid
        self.assertTrue(check_values, "1d4>=3r", lowest=1,
                        highest=4)  # Hard to tell if valid
        self.assertTrue(check_values, "1d4<=3r", lowest=1,
                        highest=4)  # Hard to tell if valid

    def test_clamping_rolls(self):
        print("\n== Clamping ==")
        spread("(1d100 + 1d100)>50")
        spread("(1d100 + 1d100)<50")
        spread("(1d100 + 1d100)<=50")
        spread("(1d100 + 1d100)>=50")

    def test_success_count(self):
        print("\n== Counting Successes ==")
        # Count how many rolls were >15
        self.assertTrue(check_values, "10d20>15£")
        self.assertTrue(check_values, "100dF£")   # Count fate dice successes

    def test_rerolls(self):
        print("\n== Re-Rolling ==")
        self.assertTrue(check_values, "30d20<15r", lowest=2,
                        highest=13)  # Reroll any <15 once
        # Reroll any <15 until no more exist
        self.assertTrue(check_values, "30d20<15R", lowest=2, highest=13)
        self.assertTrue(check_values, "30d20<15r2", lowest=2,
                        highest=13)  # Reroll any <15 twice
        # Count how many >15 after rerolling any <15 twice
        self.assertTrue(check_values, "30d20<15r2>15£", lowest=2, highest=13)
        # Count how many >15 after rerolling until they are all left (30)
        self.assertTrue(check_values, "30d20<16R>15£", lowest=2, highest=13)
        self.assertTrue(check_values, "30d20#1r", lowest=2,
                        highest=13)  # Reroll any 1s once
        self.assertTrue(check_values, "30d20#10r", lowest=2,
                        highest=13)  # Reroll any 10s once
        self.assertTrue(check_values, "30d20#10r2", lowest=2,
                        highest=13)  # Reroll any 10s twice
        # Reroll any 10s until there are none
        self.assertTrue(check_values, "30d20#10R", lowest=2, highest=13)
        # Reroll all dice if total is less than 70
        self.assertTrue(check_values, "((4d6D)@7)<70R", lowest=2, highest=13)
        # Reroll all dice if total is less than 70
        self.assertTrue(check_values, "((4d6D<8R)@7)<70R",
                        lowest=2, highest=13)

    def test_subsets_of_rolls(self):
        print("\n== Subsets ==")
        self.assertTrue(check_values, "2d20-L", lowest=2, highest=14)
        self.assertTrue(check_values, "2d20-H", lowest=2, highest=14)
        self.assertTrue(check_values, "3d20-2H", lowest=2, highest=14)
        self.assertTrue(check_values, "3d20-2L", lowest=2, highest=14)
        self.assertTrue(check_values, "3d20-3H", lowest=2, highest=14)
        self.assertTrue(check_values, "3d20-4H", lowest=2, highest=14)

        self.assertTrue(check_values, "2d20kl", lowest=2, highest=14)
        self.assertTrue(check_values, "2d20k", lowest=2, highest=14)
        self.assertTrue(check_values, "2d20kh", lowest=2, highest=14)
        self.assertTrue(check_values, "3d20k2", lowest=2, highest=14)
        self.assertTrue(check_values, "3d20kl2", lowest=2, highest=14)
        self.assertTrue(check_values, "3d20kh3", lowest=2, highest=14)
        self.assertTrue(check_values, "3d20kl4", lowest=2, highest=14)

        self.assertTrue(check_values, "2d20Dh", lowest=2, highest=14)
        self.assertTrue(check_values, "2d20D", lowest=2, highest=14)
        self.assertTrue(check_values, "3d20D", lowest=2, highest=14)
        self.assertTrue(check_values, "3d20Dh", lowest=2, highest=14)
        self.assertTrue(check_values, "3d20D3", lowest=2, highest=14)
        self.assertTrue(check_values, "3d20Dh3", lowest=2, highest=14)
        self.assertTrue(check_values, "10d20D3", lowest=2, highest=14)
        self.assertTrue(check_values, "10d20Dh3", lowest=2, highest=14)
        self.assertTrue(check_values, "3d20D4", lowest=2, highest=14)
        self.assertTrue(check_values, "3d20Dh4", lowest=2, highest=14)

    def test_custom_dice(self):
        print("\n== Custom Dice ==")
        self.assertTrue(check_values, "d{1,2,3,4,5,6}", lowest=1, highest=6)
        self.assertTrue(check_values, "d{1..6}", lowest=1, highest=6)
        self.assertTrue(check_values, "d{1,2,2,3,3,3} ", lowest=1, highest=3)
        self.assertTrue(check_values, "d{-1..1} ", lowest=-1, highest=1)
        self.assertTrue(
            check_values, "@EXTRA_CRIT_DICE=d{1,1,1,1,1..20,20,20,20,20}; ",
            lowest=-1, highest=1)
        self.assertTrue(
            check_values, "@EXTRAORDINARY_CRIT=d{1..20,100} ; ",
            lowest=-1, highest=1)
        self.assertTrue(
            check_values, "@EXTRAORDINARY_CRIT = d{1..20,100} ; ",
            lowest=-1, highest=1)
        self.assertTrue(
            check_values, "@dFailure=d{1,1,1,1,1..20} ; @dFailure  ",
            lowest=-1, highest=1)
        self.assertTrue(
            check_values, "@dFailure=d{1, 1,1,1,1..20} ; 5@dFailure<2c  ",
            lowest=-1, highest=1)
        self.assertTrue(
            check_values, "@dFailure=d{1,1 ,1,1,1..20} ; 5@dFailure#1c  ",
            lowest=-1, highest=1)
        self.assertTrue(
            check_values, "@dFailure=d{1,1,1,1,1..20} ; 5@dFailure#20r#1c  ",
            lowest=-1, highest=1)
        self.assertTrue(
            check_values, "@dFailure=d{1,1,1,1,1 .. 20} ; 5@dFailure#20R#1c  ",
            lowest=-1, highest=1)
        self.assertRaises(InvalidDiceRoll, check_values,
                          "@dEmpty=d{} ; @dEmpty", lowest=-1, highest=1)
        self.assertRaises(InvalidDiceRoll, check_values,
                          "@dEmpty=d{} ;", lowest=-1, highest=1)
        self.assertTrue(check_values, "@dStat=4d6D<7R;  ",
                        lowest=-1, highest=1)
        self.assertTrue(
            check_values, "@dStat=4d6D<7R ; @dStat@7D<70R  ",
            lowest=-1, highest=1)
        self.assertTrue(check_values, "@A=d5 ; @B=9d2;  @A*@B ",
                        lowest=9, highest=90)

    def test_conditionals(self):
        print("\n== Conditionals ==")
        # self.assertTrue(check_values,"d2?0=d4:1=d6", lowest=0, highest=6)

    def test_fate_dice(self):
        print("\n== Fate Dice ==")
        self.assertTrue(check_values, "dF", lowest=-1, highest=1)
        self.assertTrue(check_values, "1dF", lowest=-1, highest=1)
        self.assertTrue(check_values, "3dF", lowest=-3, highest=3)
        self.assertTrue(check_values, "dF+dF", lowest=-2, highest=2)
        self.assertTrue(check_values, "10dF-2dF", lowest=-8, highest=8)
        self.assertTrue(check_values, "2dF-20dF", lowest=18, highest=-18)
        self.assertTrue(check_values, "d100+dF", lowest=0, highest=101)
        self.assertTrue(check_values, "3d100@3dF", lowest=4, highest=28)
        self.assertTrue(check_values, "3df!", lowest=-3, highest=60)

    def test_exploding_dice(self):
        print("\n== Exploding & Imploding ==")
        self.assertTrue(check_values, "d3!", lowest=1, highest=60)
        self.assertTrue(check_values, "dF!", lowest=-1, highest=20)
        self.assertRaises(InvalidDiceRoll, check_values,
                          "@d3!!!", lowest=-1, highest=1)
        self.assertTrue(check_values, "d100>75!", lowest=4, highest=28)
        self.assertRaises(InvalidDiceRoll, check_values,
                          "d3~", lowest=20, highest=3)
        self.assertTrue(check_values, "dF~", lowest=-20, highest=1)
        self.assertRaises(InvalidDiceRoll, check_values,
                          "@d3~~~", lowest=-1, highest=1)
        self.assertTrue(check_values, "d100<75~", lowest=4, highest=28)
        self.assertRaises(InvalidDiceRoll, check_values,
                          "d1~", lowest=20, highest=3)
        self.assertRaises(InvalidDiceRoll, check_values,
                          "d1!", lowest=20, highest=3)
        self.assertRaises(InvalidDiceRoll, check_values,
                          "d0!", lowest=20, highest=3)
        self.assertRaises(InvalidDiceRoll, check_values,
                          "d0~", lowest=20, highest=3)


if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reports'))
