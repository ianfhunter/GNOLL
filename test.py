import numpy as np
import matplotlib.pyplot as plt
import unittest
from unittest.mock import patch

from random import randint
from dice import roll


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
    print(".", end="")

    data = spread(roll_text)

    expected = np.arange(lowest, highest+1)
    data = np.unique(np.array(data).flatten())
    if debug:
        print(data, expected)
    return np.array_equal(data, expected), data, expected, roll_text


class TestSuite(unittest.TestCase):

    def setup(self):
        np.random.seed(1)
        random.seed(1)
    
    def tearDown(self):
        pass

    def assertTrue(self, packed_test):
        cond, a, b, s = packed_test
        try:
            super(TestSuite, self).assertTrue(cond)
        except AssertionError:
            print("Fail ["+s+"] - ", a, "!=", b)
            raise AssertionError


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
        self.assertTrue(check_values("2d4", lowest=2, highest=8))
        self.assertTrue(check_values("4d4", lowest=4, highest=16))
        self.assertTrue(check_values("5d4", lowest=5, highest=20))

        # self.assertFalse(spread("0d100"))

    def test_questionable_input(self):
        pass
    #     spread("1d1")
    #     spread("1")
    #     spread("d")
    #     spread("1d0", fail=True)
    #     spread("1d", fail=True)
    #     spread("1d-1", fail=True)

    def test_rolls_with_arithmetic(self):
        print("\n== Arithmetic ==")
        self.assertTrue(check_values("1d4+1d6", lowest=2, highest=10))
        self.assertTrue(check_values("2d4+1d6", lowest=3, highest=14))
        self.assertTrue(check_values("1d4+2", lowest=3, highest=6))
        self.assertTrue(check_values("1d4-2", lowest=-1, highest=2))
        self.assertTrue(check_values("1d4*2", lowest=2, highest=8))
        self.assertTrue(check_values("1d4/2", lowest=0, highest=2))
        self.assertTrue(check_values("1d4|2", lowest=1, highest=2))
        self.assertTrue(check_values("1d4 + 1d6", lowest=2, highest=10))
        self.assertTrue(check_values("  1d4 + 1d6 ", lowest=2, highest=10))
        self.assertTrue(check_values("1d3+1d6+1d20", lowest=3, highest=29))
        self.assertTrue(check_values("1d3+1d6 + 1d20", lowest=3, highest=29))
        # self.assertTrue(check_values("1d4-2>=0", lowest=0, highest=4))
        # self.assertTrue(check_values("1d4+-1", lowest=1, highest=4))
        # spread("1d4+2")
        # spread("1d4+-2")
        # spread("1d4+-+-+-+-2")
        # spread("1d4-(2)")
        # spread("1d4x2") #Double the Value
        # spread("(1d4+1d10)*2") #Roll Twice

    def test_subsets_of_rolls(self):
        pass
    #     spread("2d20-L")
    #     spread("2d20-H")
    #     spread("3d20-2H")
    #     spread("3d20-2L")
    #     spread("3d20-3H")
    #     spread("3d20-4H", fail=True)
    #     spread("(7d6-L)x7-L")

    def test_basic_fate_dice(self):
        pass
    #     spread("dF")
    #     spread("1dF")
    #     spread("3dF")

    def test_exploding_dice(self):
        pass
        # spread("d3!")
        # spread("d6!")
        # spread("d6!!")
        # spread("d6!!!!")

    def test_advanced_fate_dice(self):
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
