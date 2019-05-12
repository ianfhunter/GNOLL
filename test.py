#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import unittest
import xmlrunner

from dice import roll, GrammarParsingException, InvalidDiceRoll

from contextlib import contextmanager
import os
import sys
import csv
import glob


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


supported = 0
unsupported = 0


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
            global unsupported
            unsupported += 1

        if cond:

            global supported
            supported += 1
            print("✓", end="")

    def assertRaises(self, fn, *args, **kwargs):
        # override to reduce print noise
        cond = True
        global supported
        with suppress_prints():
            try:
                super(TestSuite, self).assertRaises(fn, *args, kwargs)
            except NotImplementedError:
                print(u'\u231B', end="")
                cond = False

                global unsupported
                unsupported += 1

        if cond:
            supported += 1
            print("✓", end="")

    def addFailure(self, test, err):
        # here you can do what you want to do when a test case fails
        print('\n\n\ntest failed!')
        super(TestSuite, self).addFailure(test, err)

    def getMetaInfo(self, fname):
        path = "tests/meta_test_info.csv"

        if '/' in fname:
            fname = fname.split('/')[-1]

        with open(path, mode="r") as testfile:
            reader = csv.DictReader(testfile)
            for x in reader:
                if x["filename"] == fname:
                    return x

            print("Not found in meta")

    def run_tests_from_file(self, path, debug=False):

        print("\n==", self.getMetaInfo(path)["printname"], "==")

        with open(path, mode="r") as testfile:
            reader = csv.DictReader(testfile)
            for x in reader:

                if debug:
                    print("\n>", x["roll"], "[", testfile, "]")

                if x["errors"].strip() == "True":
                    self.assertRaises((InvalidDiceRoll,
                                       GrammarParsingException),
                                      check_values,
                                      x["roll"],
                                      lowest=int(x["low"]),
                                      highest=int(x["high"]))
                else:
                    self.assertTrue(check_values,
                                    x["roll"],
                                    lowest=int(x["low"]),
                                    highest=int(x["high"]))

    def test_language_independant_dice(self):
        path = "tests/"
        tests = glob.glob(path+"test*.csv")
        for f in tests:
            self.run_tests_from_file(f)
        print("\n")
        global supported
        global unsupported
        print(supported, "Supported,", unsupported, "Unsupported")


if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reports'))
