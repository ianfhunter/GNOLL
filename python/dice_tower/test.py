#!/usr/bin/env python3

import unittest
import xmlrunner

from dice_tower.dice import GrammarParsingException, InvalidDiceRoll
from dice_tower.utils import check_values, suppress_prints, display

import csv
import os
import subprocess
import sys

supported = 0
unsupported = 0

unsupported_list = []

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
            global unsupported_list
            unsupported += 1
            unsupported_list.append(args)

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

    def run_tests_from_file(self, path, debug=False, filename="", meta_file_name="meta_test_info.csv"):

        print("\n==", getMetaInfo(path, filename, meta_file_name)["printname"], "==")

        with open(os.path.join(path, filename), mode="r") as testfile:
            reader = csv.DictReader(
                filter(lambda row: row[0] != '#', testfile))
            # reader = csv.DictReader(testfile)
            for x in reader:

                if debug:
                    print("\n>", x["roll"], "[", testfile.name, "]")

                try:
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
                except Exception as e:
                    print("✗")
                    print("Exception ", e, "["+x["roll"]+"]: ")

    def test_language_independant_dice(self):
        fp = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(fp, "../../tests/")

        fname = "meta_test_info.csv"
        mpath = path + fname

        with open(mpath, mode="r") as testfile:
            reader = csv.DictReader(
                filter(lambda row: row[0] != '#', testfile))
            for x in reader:
                self.run_tests_from_file(path, filename=x["filename"], meta_file_name=fname)

        print("\n")
        global supported
        global unsupported
        print(supported, "Supported,", unsupported, "Unsupported")

        if "-v" in sys.argv:
            print("Support needed for:")
            for x in unsupported_list:
                print("> ", x[0])

    def test_cmdline(self):

        fp = os.path.dirname(os.path.realpath(__file__))
        fp = os.path.join(fp, "dice.py")
        output = subprocess.check_output(["python3", fp, "1d4", "-Q"])
        output = output.decode('ascii')
        val = int(output.split(":")[1])
        self.assertIn(val, range(1, 5))

        output = subprocess.check_output(["python3", fp, "1d4", "-D"])
        # output = output.decode('ascii')
        # val = int(output.split(":")[1])
        # self.assertIn(val, range(1, 5))

    def test_display(self):
        display("1d4")
        self.assertIn("1d4.png", os.listdir("."))


def getMetaInfo(path, fname, meta_name):
    # TODO: Absolute Path
    meta_file = path + meta_name

    with open(meta_file, mode="r") as testfile:
        reader = csv.DictReader(filter(lambda row: row[0] != '#', testfile))
        for x in reader:
            if x["filename"] == fname:
                return x

        print("Not found in meta")


if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reports'))
