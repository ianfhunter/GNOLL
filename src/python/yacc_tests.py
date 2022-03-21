#!/usr/bin/env python3

import pytest
import csv
import os
import subprocess
import sys

PY_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/python'))
print(PY_DIR)
sys.path.append(PY_DIR)

from yacc_wrapper import roll

def generate_test_cases():
    this_dir = os.path.dirname(os.path.realpath(__file__))
    csv_test_dir = os.path.join(this_dir, "../../tests")
    test_files = os.listdir(csv_test_dir)

    test=[]

    for f in test_files:
        with open(os.path.join(csv_test_dir, f)) as test_csv:
            reader = csv.DictReader(
                filter(
                    lambda row: row[0] != '#', test_csv
                )
            )
            for x in reader:
                if x["passes"].strip() == "True":
                    test.append((
                            x["roll"],
                            x["low"],
                            x["high"],
                            True,
                            f
                        )
                    )
                else:
                    test.append((
                            x["roll"],
                            x["low"],
                            x["high"],
                            False,
                            f
                        )
                    )

    return test


def try_roll(roll_text, lowest=0, highest=0, debug=False):
    code, value = roll(roll_text)
    assert(code == 0)
    assert(value >= lowest)
    assert(value <= highest)


@pytest.mark.parametrize("test_case,low,high,is_pass,testfile", generate_test_cases())
def test_all_rolls(test_case, low, high, is_pass, testfile):
    """
    Rolls that are meant to fail
    """
    try_roll(
        test_case,
        lowest=int(low),
        highest=int(high)
    )
