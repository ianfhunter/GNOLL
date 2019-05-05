import numpy as np
import matplotlib.pyplot as plt
import unittest
from unittest.mock import patch

from random import randint
from dice import roll

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
    print("✓", end="")

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

    def assertTrue(self, packed_test):
        # Override to provide error info upon failure
        cond, a, b, s = packed_test
        try:
            super(TestSuite, self).assertTrue(cond)
        except AssertionError:
            print("Fail ["+s+"] - ", a, " did not equal expected value: ", b)
            raise AssertionError

    def assertRaises(self, fn, *args, **kwargs):
        # override to reduce print noise
        with suppress_prints():
            super(TestSuite, self).assertRaises(fn, *args, kwargs)

    def addFailure(self, test, err):
        # here you can do what you want to do when a test case fails 
        print('\n\n\ntest failed!')
        super(TestSuite, self).addFailure(test, err)

    def test_single_dice(self):
        print("\n== Single Dice ==")
        self.assertTrue(check_values("d4", lowest=1, highest=4))
        self.assertTrue(check_values("1d4", lowest=1, highest=4))
        self.assertTrue(check_values("1d6", lowest=1, highest=6))
        self.assertTrue(check_values("1d8", lowest=1, highest=8))
        self.assertTrue(check_values("1d10", lowest=1, highest=10))
        self.assertTrue(check_values("1d12", lowest=1, highest=12))
        self.assertTrue(check_values("1d20", lowest=1, highest=20))
        self.assertTrue(check_values("1d100", lowest=1, highest=100))
        self.assertTrue(check_values(" 1d100 ", lowest=1, highest=100))

    def test_multiple_dice(self):
        print("\n== Multiple Dice ==")
        self.assertTrue(check_values("d4", lowest=1, highest=4))
        self.assertTrue(check_values("2d4", lowest=2, highest=8))
        self.assertTrue(check_values("4d4", lowest=4, highest=16))
        self.assertTrue(check_values("5d4", lowest=5, highest=20))

    def test_questionable_input(self):
        print("\n== Odd Cases ==")
        self.assertTrue(check_values("0", lowest=0, highest=0))
        self.assertTrue(check_values("0d0", lowest=0, highest=0))
        self.assertTrue(check_values("-1d0", lowest=0, highest=0))
        self.assertTrue(check_values("1-d1", lowest=0, highest=0))
        self.assertTrue(check_values("1d1", lowest=1, highest=1))

        self.assertRaises(ValueError, check_values, "0d", lowest=1, highest=4)
        self.assertRaises(Exception, check_values, "1d-1", lowest=0, highest=0)
        self.assertRaises(Exception, check_values, "d", lowest=0, highest=0)

    def test_rolls_with_arithmetic(self):
        print("\n== Arithmetic ==")
        self.assertTrue(check_values("d4+d4", lowest=2, highest=8))
        # Doesn't quite work as face min != min result
        self.assertTrue(check_values("d4+-d4", lowest=0, highest=0))
        self.assertTrue(check_values("1d4+1d6", lowest=2, highest=10))
        self.assertTrue(check_values("2d4+1d6", lowest=3, highest=14))
        self.assertTrue(check_values("1d4+2", lowest=3, highest=6))
        self.assertTrue(check_values("1d4-2", lowest=-1, highest=2))
        self.assertTrue(check_values("1d4*2", lowest=2, highest=8))
        self.assertTrue(check_values("1d4/2", lowest=0, highest=2))
        self.assertTrue(check_values("1d4|2", lowest=1, highest=2))
        self.assertTrue(check_values("1d4 + 1d6", lowest=2, highest=10))
        self.assertTrue(check_values("  1d4 + 1d6 ", lowest=2, highest=10))
        self.assertTrue(check_values("1d4+-1", lowest=0, highest=3))
        self.assertTrue(check_values("1d4+-2", lowest=-1, highest=2))
        self.assertTrue(check_values("1d4+----2", lowest=3, highest=6))
        self.assertTrue(check_values("1d4----2", lowest=3, highest=6))
        self.assertTrue(check_values("1d3+1d6+1d20", lowest=3, highest=29))
        self.assertTrue(check_values("1d3+1d6 + 1d20", lowest=3, highest=29))
        self.assertTrue(check_values("1+1", lowest=2, highest=2))
        self.assertTrue(check_values("1+(1)", lowest=2, highest=2))
        self.assertTrue(check_values("1d4-(2)", lowest=-1, highest=2))

        # self.assertTrue(check_values("1d4-2>=0", lowest=0, highest=4))
        # spread("1d4x2") #Double the Value
        # spread("(1d4+1d10)*2") #Roll Twice
        # spread("(1d4+1d10)x2") #Roll Twice


    def test_roll_sequences(self):
        print("\n== Sequences ==")
        # spread("(1d4+1d10)x2") #Roll Twice
        # spread("1d4, 1d10") #Roll Twice
        # spread("(1d4, 1d10)", fail=True) #Roll Twice


    def test_clamping_rolls(self):
        print("\n== Clamping ==")
        # spread("(1d100 + 1d100)>50")
        # spread("(1d100 + 1d100)<50")
        # spread("(1d100 + 1d100)<=50")
        # spread("(1d100 + 1d100)>=50")

    def test_success_count(self):
        print("\n== Counting Successes ==")
        # spread("10d20>15c")   # Count how many rolls were >15
        # spread("100dFc")   # Count fate dice successes

    def test_rerolls(self):
        print("\n== Re-Rolling ==")
        # spread("30d20<15r")   #Reroll any <15 once
        # spread("30d20<15R")   #Reroll any <15 until no more exist
        # spread("30d20<15r2")  #Reroll any <15 twice
        # spread("30d20<15r2>15c")  #Count how many >15 after rerolling any <15 twice
        # spread("30d20<16R>15c")  #Count how many >15 after rerolling until they are all left (30)
        # spread("30d20#1r")   #Reroll any 1s once
        # spread("30d20#10r")   #Reroll any 10s once
        # spread("30d20#10rr2")   #Reroll any 10s twice
        # spread("30d20#10R")   #Reroll any 10s until there are none
        # spread("((4d6D)x7)<70R")   #Reroll all dice if total is less than 70
        # spread("((4d6D<8R)x7)<70R")   #Reroll all dice if total is less than 70


    def test_subsets_of_rolls(self):
        print("\n== Subsets ==")
    #     spread("2d20-L")
    #     spread("2d20-H")
    #     spread("3d20-2H")
    #     spread("3d20-2L")
    #     spread("3d20-3H")
    #     spread("3d20-4H", fail=True)
    #     spread("(7d6-L)x7-L")

    #     spread("2d20kl")
    #     spread("2d20k")
    #     spread("2d20kh")
    #     spread("3d20k2")
    #     spread("3d20kl2")
    #     spread("3d20kh3")
    #     spread("3d20kl4", fail=True)
    #     spread("(7d6kl1)x7kl6")  


    #     spread("2d20Dh")
    #     spread("2d20D")
    #     spread("3d20D")
    #     spread("3d20Dh")
    #     spread("3d20D3")
    #     spread("3d20Dh3")
    #     spread("10d20D3")
    #     spread("10d20Dh3")
    #     spread("3d20D4", fail=True)
    #     spread("3d20Dh4", fail=True)
    #     spread("(7d6D)x7D")  



    def test_custom_dice(self):
        print("\n== Custom Dice ==")
        # d{1,2,3,4,5,6}  "d6"
        # d{1..6}  "d6"
        # d{-1..1} "Fudge die"
        # d{1,2,2,3,3,3}  "triangledice"

        # EXTRA_CRIT_DICE=d{1,1,1,1,1..20,20,20,20,20} ;
        # EXTRODINARY_CRIT=d{1..20,100} ;
        # dFailure=d{1,1,1,1,1..20} ; dFailure 
        # dFailure=d{1,1,1,1,1..20} ; 5dFailure 
        # dFailure=d{1,1,1,1,1..20} ; 5dFailure<2c   #Count failures
        # dFailure=d{1,1,1,1,1..20} ; 5dFailure#1c   #Count failures
        # dFailure=d{1,1,1,1,1..20} ; 5dFailure#20r#1c   #Count failures, reroll first 20s
        # dFailure=d{1,1,1,1,1..20} ; 5dFailure#20R#1c   #Count failures, reroll all 20s
        # dEmpty=d{} - Failure Empty Set

        # dStat=4d6D<7R ; dStatx7D<70R


    def test_conditionals(self):
        print("\n== Conditionals ==")
        # d2?0=d4:1=d6

    def test_basic_fate_dice(self):
        print("\n== Fate ==")
    #     spread("dF")
    #     spread("1dF")
    #     spread("3dF")

    def test_exploding_dice(self):
        print("\n== Exploding ==")
        pass
        # Reroll and add on a maximum (! for maximum rolls)
        # spread("d3!")
        # spread("d6!")
        # spread("d6!!")
        # spread("d6!!!!")

    def test_advanced_fate_dice(self):
        print("\n== Fate Die - Advanced ==")
        pass
    #     spread("d100xd100")
    #     spread("d100+dF")
    #     spread("3d100x3dF")

    #     spread("1dF!")

if __name__ == "__main__":
    unittest.main()
    # a = "d6"
    # res = roll(a)
    # print(res)
    # res = spread(a)
    # print(np.unique(np.array(res).flatten()))
