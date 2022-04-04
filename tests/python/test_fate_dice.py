#!/usr/bin/env python3

from unittest import mock
import pytest
import csv
import os
import sys
from util import roll, Mock

def test_fate():
    # Assure Symbols are correct
    # TODO: Maybe it would be better to return "PLUS", "ZERO" "MINUS"?
    result = roll("dF", mock_mode=Mock.RETURN_CONSTANT, mock_const=0)
    assert(result == "+")
    result = roll("dF", mock_mode=Mock.RETURN_CONSTANT, mock_const=1)
    assert(result == 0)
    result = roll("dF", mock_mode=Mock.RETURN_CONSTANT, mock_const=2)
    assert(result == "-")

def test_multidie():
    result = roll("2dF", mock_mode=Mock.RETURN_CONSTANT, mock_const=2)
    assert(result == "--")

def test_fate_addition():
    # Addition = Concatination
    result = roll("df+df", mock_mode=Mock.RETURN_CONSTANT, mock_const=2)
    assert(result == "--")

# @pytest.mark.skip(reason="Not supported yet and may cause memory issue")
@pytest.mark.xfail()
def test_fate_subtraction():
    # Subtraction = Removing common elements IF PRESENT
    result = roll("3dF-dF", mock_mode=Mock.RETURN_CONSTANT, mock_const=2)
    assert(result == "--")
    result = roll("dF-dF", mock_mode=Mock.RETURN_INCREMENTING)
    assert(result == "+")


# @pytest.mark.skip(reason="Not supported yet and may cause memory issue")
@pytest.mark.xfail()
def test_fate_numeral_interoperability():
    # Most of the time, using the two together doesn't make sense
    with pytest.raises(Exception):
        result = roll("d10+dF", mock_mode=(0,1))
    with pytest.raises(Exception):
        result = roll("d10-dF", mock_mode=(0,1))

    # Multiplication and Division are ambigious
    # e.g.
    # dF * 2 could mean:
    # - roll 2 dF dice (2dF -> -+)
    # or
    # - multiply the result of dF by 2 (+ -> ++)
    # Unless there is evidence of that priority defined somewhere
    with pytest.raises(Exception):
        result = roll("dF*2")
    with pytest.raises(Exception):
        result = roll("dF*dF")
    with pytest.raises(Exception):
        result = roll("dF/2")
    with pytest.raises(Exception):
        result = roll("dF/dF")
    with pytest.raises(Exception):
        # We could perhaps use modulo as a counter
        # or some other function.
        # But for now, its undefined behaviour
        result = roll("dF%2")
    with pytest.raises(Exception):
        result = roll("dF%dF")
