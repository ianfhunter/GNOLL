#!/usr/bin/env python3

import pytest
import csv
import os
import subprocess
import sys

PY_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/python'))
sys.path.append(PY_DIR)

from yacc_wrapper import roll

def generate_test_cases(f):
    this_dir = os.path.dirname(os.path.realpath(__file__))
    csv_test_dir = os.path.join(this_dir, "../../tests")
    test_file = os.path.join(csv_test_dir, f) + ".csv"

    test = []
    with open(test_file) as test_csv:
        reader = csv.DictReader(
            filter(
                lambda row: row[0] != '#', test_csv
            )
        )
        for x in reader:
            if x["passes"].strip().lower() == "true":
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
    print("Rolling:", roll_text)
    code, value = roll(roll_text)
    assert(code == 0)
    assert(value >= lowest)
    assert(value <= highest)

def core_test_logic(test_case, low, high, is_pass):
    if is_pass:
        try_roll(
            test_case,
            lowest=int(low),
            highest=int(high)
        )
    else:
        with pytest.raises(Exception):
            try_roll(
                test_case,
                lowest=int(low),
                highest=int(high)
            )

@pytest.mark.parametrize("test_case,low,high,is_pass,testfile", generate_test_cases("test_sided_dice"))
def test_sided_dice(test_case, low, high, is_pass, testfile):
    core_test_logic(test_case, low, high, is_pass)

@pytest.mark.xfail
@pytest.mark.parametrize("test_case,low,high,is_pass,testfile", generate_test_cases("test_fate_dice"))
def test_fate_dice(test_case, low, high, is_pass, testfile):
    core_test_logic(test_case, low, high, is_pass)

@pytest.mark.parametrize("test_case,low,high,is_pass,testfile", generate_test_cases("test_dropping"))
def test_dropping(test_case, low, high, is_pass, testfile):
    core_test_logic(test_case, low, high, is_pass)

@pytest.mark.parametrize("test_case,low,high,is_pass,testfile", generate_test_cases("test_numbers"))
def test_numbers(test_case, low, high, is_pass, testfile):
    core_test_logic(test_case, low, high, is_pass)

@pytest.mark.parametrize("test_case,low,high,is_pass,testfile", generate_test_cases("test_arithmetic"))
def test_arithmetic(test_case, low, high, is_pass, testfile):
    core_test_logic(test_case, low, high, is_pass)


@pytest.mark.xfail
@pytest.mark.parametrize("test_case,low,high,is_pass,testfile", generate_test_cases("test_current_outliers"))
def test_current_outliers(test_case, low, high, is_pass, testfile):
    core_test_logic(test_case, low, high, is_pass)

@pytest.mark.xfail
@pytest.mark.parametrize("test_case,low,high,is_pass,testfile", generate_test_cases("test_clamping"))
def test_clamping(test_case, low, high, is_pass, testfile):
    core_test_logic(test_case, low, high, is_pass)

@pytest.mark.xfail
@pytest.mark.parametrize("test_case,low,high,is_pass,testfile", generate_test_cases("test_conditions"))
def test_conditions(test_case, low, high, is_pass, testfile):
    core_test_logic(test_case, low, high, is_pass)

@pytest.mark.xfail
@pytest.mark.parametrize("test_case,low,high,is_pass,testfile", generate_test_cases("test_count_successes"))
def test_count_successes(test_case, low, high, is_pass, testfile):
    core_test_logic(test_case, low, high, is_pass)

@pytest.mark.xfail
@pytest.mark.parametrize("test_case,low,high,is_pass,testfile", generate_test_cases("test_explosions"))
def test_explosions(test_case, low, high, is_pass, testfile):
    core_test_logic(test_case, low, high, is_pass)

@pytest.mark.xfail
@pytest.mark.parametrize("test_case,low,high,is_pass,testfile", generate_test_cases("test_macros"))
def test_macros(test_case, low, high, is_pass, testfile):
    core_test_logic(test_case, low, high, is_pass)

@pytest.mark.xfail
@pytest.mark.parametrize("test_case,low,high,is_pass,testfile", generate_test_cases("test_groups"))
def test_groups(test_case, low, high, is_pass, testfile):
    core_test_logic(test_case, low, high, is_pass)

@pytest.mark.xfail
@pytest.mark.parametrize("test_case,low,high,is_pass,testfile", generate_test_cases("test_multiple_dice"))
def test_multiple_dice(test_case, low, high, is_pass, testfile):
    core_test_logic(test_case, low, high, is_pass)

@pytest.mark.xfail
@pytest.mark.parametrize("test_case,low,high,is_pass,testfile", generate_test_cases("test_odd_inputs"))
def test_odd_inputs(test_case, low, high, is_pass, testfile):
    core_test_logic(test_case, low, high, is_pass)

@pytest.mark.xfail
@pytest.mark.parametrize("test_case,low,high,is_pass,testfile", generate_test_cases("test_rerolling"))
def test_rerolling(test_case, low, high, is_pass, testfile):
    core_test_logic(test_case, low, high, is_pass)

@pytest.mark.xfail
@pytest.mark.parametrize("test_case,low,high,is_pass,testfile", generate_test_cases("test_sequences"))
def test_sequences(test_case, low, high, is_pass, testfile):
    core_test_logic(test_case, low, high, is_pass)

@pytest.mark.xfail
@pytest.mark.parametrize("test_case,low,high,is_pass,testfile", generate_test_cases("test_several"))
def test_several(test_case, low, high, is_pass, testfile):
    core_test_logic(test_case, low, high, is_pass)

@pytest.mark.xfail
@pytest.mark.parametrize("test_case,low,high,is_pass,testfile", generate_test_cases("test_subsets"))
def test_subsets(test_case, low, high, is_pass, testfile):
    core_test_logic(test_case, low, high, is_pass)

@pytest.mark.parametrize("test_case,low,high,is_pass,testfile", generate_test_cases("games/test_dungeons_and_dragons"))
def test_dungeons_and_dragons(test_case, low, high, is_pass, testfile):
    core_test_logic(test_case, low, high, is_pass)

@pytest.mark.parametrize("test_case,low,high,is_pass,testfile", generate_test_cases("games/test_dungeons_and_dragons_online"))
def test_dungeons_and_dragons_online(test_case, low, high, is_pass, testfile):
    core_test_logic(test_case, low, high, is_pass)
