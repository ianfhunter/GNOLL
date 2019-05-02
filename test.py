from dice import roll
import numpy as np
import matplotlib.pyplot as plt
import unittest
import random

np.random.seed(1)
random.seed(1)

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

    print("test ", s)

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

    graph(v, s)
    return True

class TestSuite(unittest.TestCase):

    def setup(self):
        pass
    
    def tearDown(self):
        pass

    def test_single_dice(self):
        spread("1d4")
        spread("1d6")
        spread("1d8")
        spread("1d10")
        spread("1d12")
        spread("1d20")
        spread("1d100")
        spread("1d1000")

    def test_multiple_dice(self):
        spread("1d100") 
        spread("2d100") 
        spread("3d100")
        spread("100d3")
        spread("0d100", fail=True) 

    def test_questionable_input(self):
        spread("1d1")
        spread("1")
        spread("1d0", fail=True)
        spread("1d", fail=True)
        spread("1d-1", fail=True)

    def test_rolls_with_arithmetic(self):
        spread("1d4+2")
        spread("1d4+-2")
        spread("1d4-2")
        spread("1d4-(2)")
        spread("1d3+1d3")
        spread("1d4x2") #Double the Value
        spread("1d4*2") #Roll Twice
        spread("(1d4+1d10)*2") #Roll Twice


    def test_subsets_of_rolls(self):
        spread("2d20-L")
        spread("2d20-H")
        spread("3d20-2H")
        spread("3d20-2L")
        spread("3d20-3H")
        spread("3d20-4H", fail=True)
        spread("(7d6-L)x7-L")

    def test_basic_fate_dice(self):
        spread("dF")
        spread("1dF")
        spread("3dF")

    def test_advanced_fate_dice(self):
        spread("d100xd100")
        spread("d100+dF")
        spread("3d100x3dF")

        spread("1dF!")

if __name__ == "__main__":
    unittest.main()
    # spread("1d4")