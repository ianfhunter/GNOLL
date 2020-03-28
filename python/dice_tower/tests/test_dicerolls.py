#!/usr/bin/env python3

import pytest
import csv
import os
import subprocess
import sys

try:
    # Local
    sys.path.append("..")
    from ..dice import GrammarParsingException, InvalidDiceRoll
    from ..utils import check_values, suppress_prints, display
except ModuleNotFoundError:
    # Pip Package
    from dice_tower.dice import GrammarParsingException, InvalidDiceRoll
    from dice_tower.utils import check_values, suppress_prints, display


def test_cmdline():
    fp = os.path.dirname(os.path.realpath(__file__))
    fp = os.path.join(fp, "../dice.py")
    output = subprocess.check_output(["python3", fp, "1d4", "--silent"])
    output = output.decode('ascii')
    val = int(output.split(":")[1])
    assert(val in range(1, 5))

    output = subprocess.check_output(["python3", fp, "1d4", "--verbose"])


def test_display():
    display("1d4")
    assert("1d4.png" in os.listdir("."))


def generate_test_cases(which="TP"):
    this_dir = os.path.dirname(os.path.realpath(__file__))
    csv_test_dir = os.path.join(this_dir, "../../../tests/")
    test_files = os.listdir(csv_test_dir)

    true_positive_tests = []
    true_negative_tests = []

    for f in test_files:
        with open(os.path.join(csv_test_dir, f)) as test_csv:
            reader = csv.DictReader(
                filter(
                    lambda row: row[0] != '#', test_csv
                )
            )
            for x in reader:
                if x["errors"].strip() == "True":
                    true_negative_tests.append((
                            x["roll"],
                            x["low"],
                            x["high"],
                            f
                        )
                    )
                else:
                    true_positive_tests.append((
                            x["roll"],
                            x["low"],
                            x["high"],
                            f
                        )
                    )

    if which == "TP":
        return true_positive_tests
    elif which == "FP":
        return true_negative_tests



@pytest.mark.parametrize("test_case,low,high,testfile", generate_test_cases("FP"))
def test_bad_dice_rolls(test_case, low, high, testfile):
    """
    Rolls that are meant to fail
    """
    with pytest.raises(
        (InvalidDiceRoll, GrammarParsingException)
    ):
        try:
            check_values(
                test_case,
                lowest=low,
                highest=high
            )

        except NotImplementedError:
            pytest.xfail("Not Implemented Yet")

@pytest.mark.parametrize("test_case,low,high,testfile", generate_test_cases("TP"))
def test_good_dice_rolls(test_case, low, high, testfile):
    """
    Rolls that should pass
    """
    try:
        assert(
            check_values(
                test_case,
                lowest=low,
                highest=high
            )
        )
    except NotImplementedError:
        pytest.xfail("Not Implemented Yet")

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
