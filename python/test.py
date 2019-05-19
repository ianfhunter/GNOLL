#!/usr/bin/env python3

import unittest
import xmlrunner

from dice import GrammarParsingException, InvalidDiceRoll
from utils import check_values, suppress_prints

import csv
import glob

supported = 0
unsupported = 0


class TestSuite(unittest.TestCase):

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

    def run_tests_from_file(self, path, debug=False):

        print("\n==", getMetaInfo(path)["printname"], "==")

        with open(path, mode="r") as testfile:
            reader = csv.DictReader(filter(lambda row: row[0]!='#', testfile))
            # reader = csv.DictReader(testfile)
            for x in reader:

                if debug:
                    print("\n>", x["roll"], "[", testfile, "]")

                if x["errors"].strip() == "True":
                    self.assertRaises((InvalidDiceRoll,
                                       GrammarParsingException),
                                      check_values,
                                      x["roll"],
                                      lowest=x["low"],
                                      highest=x["high"])
                else:
                    self.assertTrue(check_values,
                                    x["roll"],
                                    lowest=x["low"],
                                    highest=x["high"])

    def test_language_independant_dice(self):
        path = "../tests/"
        tests = glob.glob(path+"test*.csv")
        for f in tests:
            self.run_tests_from_file(f)
        print("\n")
        global supported
        global unsupported
        print(supported, "Supported,", unsupported, "Unsupported")


def getMetaInfo(fname):
    # TODO: Absolute Path
    path = "../tests/meta_test_info.csv"

    if '/' in fname:
        fname = fname.split('/')[-1]

    with open(path, mode="r") as testfile:
        reader = csv.DictReader(testfile)
        for x in reader:
            if x["filename"] == fname:
                return x

        print("Not found in meta")


if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reports'))
