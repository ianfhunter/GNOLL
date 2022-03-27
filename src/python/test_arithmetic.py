#!/usr/bin/env python3

from unittest import mock
import pytest
import csv
import os
import sys
from util import test_roll

def test_numbers():
    # Just Numbers
    result = test_roll("4")
    assert(result == 4)

    result = test_roll("-4")
    assert(result == -4)

def test_addition():
    result = test_roll("4+3")
    assert(result == 7)

    result = test_roll("4+(3)")
    assert(result == 7)

    result = test_roll("4+2d4", mock_random=7)
    assert(result == 11)

    result = test_roll("2d4+4", mock_random=7)
    assert(result == 11)

    result = test_roll("d4+1d4", mock_random=3)
    assert(result == 6)

def test_subtraction():
    result = test_roll("-d40", mock_random=3)
    assert(result == 3)

    result = test_roll("4-3")
    assert(result == 1)

    result = test_roll("4--3")
    assert(result == 7)

    result = test_roll("---------------4")
    assert(result == -4)
    result = test_roll("----------------4")
    assert(result == 4)

    result = test_roll("4-2d4", mock_random=7)
    assert(result == -3)

    result = test_roll("2d4-4", mock_random=7)
    assert(result == 3)

    result = test_roll("2d4-d4", mock_random=3)
    assert(result == 3)

def test_multiplication():
    result = test_roll("1d4*2", mock_random=3)
    assert(result == 6)

    result = test_roll("(1d4+1d10)*2", mock_random=3)
    assert(result == 12)

def test_division():
    # Round Down
    result = test_roll("1d4/2", mock_random=1)
    assert(result == 0)
    # Round Up
    result = test_roll("1d4\2", mock_random=1)
    assert(result == 1)


def test_modulo():
    result = test_roll("1d4%2", mock_random=3)
    assert(result == 1)
    result = test_roll("1d4%2", mock_random=4)
    assert(result == 0)

