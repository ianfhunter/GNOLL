#!/usr/bin/env python3

from unittest import mock
import pytest
import csv
import os
import sys
from util import roll

def test_numbers():
    # Just Numbers
    result = roll("4")
    assert(result == 4)

    result = roll("-4")
    assert(result == -4)

def test_addition():
    result = roll("4+3")
    assert(result == 7)

    result = roll("4+(3)")
    assert(result == 7)

    result = roll("4+2d4", mock_random=3)
    assert(result == 10)

    result = roll("2d4+4", mock_random=3)
    assert(result == 10)

    result = roll("d4+1d4", mock_random=3)
    assert(result == 6)

def test_subtraction():
    result = roll("-d40", mock_random=3)
    assert(result == -3)

    result = roll("4-3")
    assert(result == 1)

    result = roll("4--3")
    assert(result == 7)

    result = roll("---------------4")
    assert(result == -4)
    result = roll("----------------4")
    assert(result == 4)

    result = roll("4-2d4", mock_random=3)
    assert(result == -2)

    result = roll("2d4-4", mock_random=3)
    assert(result == 2)

    result = roll("2d4-d4", mock_random=3)
    assert(result == 3)

def test_multiplication():
    result = roll("1d4*2", mock_random=3)
    assert(result == 6)

    result = roll("(1d4+1d10)*2", mock_random=3)
    assert(result == 12)

def test_division():
    # Round Down
    result = roll("1d4/2", mock_random=1)
    assert(result == 1)
    # Round Up
    result = roll("1d4\\2", mock_random=1)
    assert(result == 0)


def test_modulo():
    result = roll("1d4%2", mock_random=3)
    assert(result == 1)
    result = roll("1d4%2", mock_random=4)
    assert(result == 0)
