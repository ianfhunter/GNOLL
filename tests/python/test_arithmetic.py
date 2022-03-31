#!/usr/bin/env python3

from unittest import mock
import pytest
import csv
import os
import sys
from util import roll, Mock

@pytest.mark.parametrize("r,out",[
    ("4", 4),
    ("-4", -4)
])
def test_numbers(r, out):
    # Just Numbers
    result = roll(r)
    assert(result == out)

@pytest.mark.parametrize("r,out,mock",[
    ("4+3", 7, Mock.NO_MOCK),
    ("4+(3)", 7, Mock.NO_MOCK),
    ("4+2d4", 10, Mock.RETURN_CONSTANT_THREE),
    ("2d4+4", 10, Mock.RETURN_CONSTANT_THREE),
    ("d4+1d4", 6, Mock.RETURN_CONSTANT_THREE),
])
def test_addition(r, out, mock):
    result = roll(r, mock_random=mock)
    assert(result == out)

@pytest.mark.parametrize("r,out,mock",[
    ("-d40", -3, Mock.RETURN_CONSTANT_THREE),
    ("4-3", 1, None),
    ("4--3", 7, None),
    ("---------------4", -4, None),
    ("----------------4", 4, None),
    ("4-2d4", -2, Mock.RETURN_CONSTANT_THREE),
    ("2d4-4", 2, Mock.RETURN_CONSTANT_THREE),
    ("2d4-d4", 3, Mock.RETURN_CONSTANT_THREE),
])
def test_subtraction(r, out, mock):
    result = roll(r, mock_random=mock)
    assert(result == out)

@pytest.mark.parametrize("r,out,mock",[
    ("1d4*2", 6, Mock.RETURN_CONSTANT_THREE),
    ("(1d4+1d10)*2", 12, Mock.RETURN_CONSTANT_THREE),
])
def test_multiplication(r, out, mock):
    result = roll(r, mock_random=mock)
    assert(result == out)

@pytest.mark.parametrize("r,out,mock",[
    ("1d4/2", 1, Mock.RETURN_CONSTANT_THREE),    # Down
    ("1d4\\2", 2, Mock.RETURN_CONSTANT_THREE),   # Up
])
def test_division(r, out, mock):
    result = roll(r, mock_random=mock)
    assert(result == out)

@pytest.mark.parametrize("r,out,mock",[
    ("1d4%2", 1, Mock.RETURN_CONSTANT_THREE),
    ("1d4%3", 0, Mock.RETURN_CONSTANT_THREE),
])
def test_modulo(r, out, mock):
    result = roll(r, mock_random=mock)
    assert(result == out)
