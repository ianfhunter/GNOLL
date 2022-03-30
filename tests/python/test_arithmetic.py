#!/usr/bin/env python3

from unittest import mock
import pytest
import csv
import os
import sys
from util import roll

@pytest.mark.parametrize("r,out",[
    ("4", 4),
    ("-4", -4)
])
def test_numbers(r, out):
    # Just Numbers
    result = roll(r)
    assert(result == out)

@pytest.mark.parametrize("r,out,mock",[
    ("4+3", 7, None),
    ("4+(3)", 7, None),
    ("4+2d4", 10, 3),
    ("2d4+4", 10, 3),
    ("d4+1d4", 6, 3),
])
def test_addition(r, out, mock):
    result = roll(r, mock_random=mock)
    assert(result == out)

@pytest.mark.parametrize("r,out,mock",[
    ("-d40", -3, 3),
    ("4-3", 1, None),
    ("4--3", 7, None),
    ("---------------4", -4, None),
    ("----------------4", 4, None),
    ("4-2d4", -2, 3),
    ("2d4-4", 2, 3),
    ("2d4-d4", 3, 3),
])
def test_subtraction(r, out, mock):
    result = roll(r, mock_random=mock)
    assert(result == out)

@pytest.mark.parametrize("r,out,mock",[
    ("1d4*2", 6, 3),
    ("(1d4+1d10)*2", 12, 3),
])
def test_multiplication(r, out, mock):
    result = roll(r, mock_random=mock)
    assert(result == out)

@pytest.mark.parametrize("r,out,mock",[
    ("1d4/2", 1, 3),    # Down
    ("1d4\\2", 0, 3),   # Up
])
def test_division(r, out, mock):
    result = roll(r, mock_random=mock)
    assert(result == out)

@pytest.mark.parametrize("r,out,mock",[
    ("1d4*2", 1, 3),
    ("1d4*2", 0, 4),
])
def test_modulo(r, out, mock):
    result = roll(r, mock_random=mock)
    assert(result == out)
