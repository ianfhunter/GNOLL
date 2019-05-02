from dice import roll
import numpy as np
import matplotlib.pyplot as plt
import unittest
import random


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

def spread(s, fail=False):

    # print("\ntest ", s)

    v = []
    for n in range(1000):
        try:
            v.append(roll(s))
        except Exception:
            if fail:
                return False
            else:
                print("Unexpected Error")
                raise Exception

    if False:
        graph(v, s)
    return v

def check_values(data, lowest=0, highest=0, debug=False):
    print(".", end="")

    expected = np.arange(lowest, highest+1)
    data = np.unique(np.array(data).flatten())
    if debug:
        print(data, expected)
    return np.array_equal(data, expected)

class TestSuite(unittest.TestCase):

    def setup(self):
        np.random.seed(1)
        random.seed(1)
    
    def tearDown(self):
        pass

    def test_single_dice(self):
        print("\n== Single Dice ==")
        self.assertTrue(check_values(spread("d4"), lowest=1, highest=4))
        self.assertTrue(check_values(spread("1d4"), lowest=1, highest=4))
        self.assertTrue(check_values(spread("1d6"), lowest=1, highest=6))
        self.assertTrue(check_values(spread("1d8"), lowest=1, highest=8))
        self.assertTrue(check_values(spread("1d10"), lowest=1, highest=10))
        self.assertTrue(check_values(spread("1d12"), lowest=1, highest=12))
        self.assertTrue(check_values(spread("1d20"), lowest=1, highest=20))
        self.assertTrue(check_values(spread("1d100"), lowest=1, highest=100))

    def test_multiple_dice(self):
        print("\n== Multiple Dice ==")
        self.assertTrue(check_values(spread("1d4"), lowest=1, highest=4))
        self.assertTrue(check_values(spread("2d4"), lowest=2, highest=8))
        self.assertTrue(check_values(spread("4d4"), lowest=4, highest=16))
        self.assertTrue(check_values(spread("5d4"), lowest=5, highest=20))

        # self.assertFalse(spread("0d100"))

    def test_questionable_input(self):
        pass
    #     spread("1d1")
    #     spread("1")
    #     spread("1d0", fail=True)
    #     spread("1d", fail=True)
    #     spread("1d-1", fail=True)

    def test_rolls_with_arithmetic(self):
        print("\n== Arithmetic ==")
        self.assertTrue(check_values(spread("1d4+1d6"), lowest=2, highest=10))
        self.assertTrue(check_values(spread("2d4+1d6"), lowest=3, highest=14))
        # self.assertTrue(check_values(spread("1d4+2"), lowest=3, highest=6))
        # self.assertTrue(check_values(spread("1d4-2"), lowest=1, highest=4))
        # self.assertTrue(check_values(spread("1d4-2>=0"), lowest=0, highest=4))
        # self.assertTrue(check_values(spread("1d4+-1"), lowest=1, highest=4))
        # spread("1d4+2")
        # spread("1d4+-2")
        # spread("1d4-2")
        # spread("1d4-(2)")
        # spread("1d3+1d3")
        # spread("1d4x2") #Double the Value
        # spread("1d4*2") #Roll Twice
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
