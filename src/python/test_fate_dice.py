#!/usr/bin/env python3

from unittest import mock
import pytest
import csv
import os
import sys
from util import test_roll

def test_fate():
    # Assure Symbols are correct
    # TODO: Maybe it would be better to return "PLUS", "ZERO" "MINUS"?
    result = test_roll("dF", mock_random=(0))
    assert(result == "-")
    result = test_roll("dF", mock_random=(1))
    assert(result == "0")
    result = test_roll("dF", mock_random=(2))
    assert(result == "+")

def test_multidie():
    result = test_roll("2dF", mock_random=(2,2))
    assert(result == "++")

@pytest.mark.xfail
def test_fate_addition():
    # Addition = Concatination
    result = test_roll("dF+dF", mock_random=(2,2))
    assert(result == "++")

def test_fate_subtraction():
    # Subtraction = Removing common elements IF PRESENT
    result = test_roll("3dF-dF", mock_random=2)
    assert(result == "++")
    result = test_roll("dF-dF", mock_random=(0,1))
    assert(result == "-")


def test_fate_numeral_interoperability():
    # Most of the time, using the two together doesn't make sense
    with pytest.raises(Exception):
        result = test_roll("d10+dF", mock_random=(0,1))
    with pytest.raises(Exception):
        result = test_roll("d10-dF", mock_random=(0,1))

    # Multiplication and Division are ambigious
    # e.g.
    # dF * 2 could mean:
    # - roll 2 dF dice (2dF -> -+) 
    # or
    # - multiply the result of dF by 2 (+ -> ++)
    # Unless there is evidence of that priority defined somewhere
    with pytest.raises(Exception):
        result = test_roll("dF*2")
    with pytest.raises(Exception):
        result = test_roll("dF*dF")
    with pytest.raises(Exception):
        result = test_roll("dF/2")
    with pytest.raises(Exception):
        result = test_roll("dF/dF")
    with pytest.raises(Exception):
        # We could perhaps use modulo as a counter 
        # or some other function.
        # But for now, its undefined behaviour
        result = test_roll("dF%2")
    with pytest.raises(Exception):
        result = test_roll("dF%dF")
