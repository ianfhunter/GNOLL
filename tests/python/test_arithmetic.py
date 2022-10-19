#!/usr/bin/env python3

import pytest
from util import Mock, roll


@pytest.mark.parametrize("r,out", [("4", 4), ("-4", -4)])
def test_numbers(r, out):
    # Just Numbers
    result = roll(r)
    assert result == out


@pytest.mark.parametrize(
    "r,out,mock",
    [
        ("4+3", 7, Mock.NO_MOCK),
        ("4+(3)", 7, Mock.NO_MOCK),
        ("4+2d4", 10, Mock.RETURN_CONSTANT),
        ("2d4+4", 10, Mock.RETURN_CONSTANT),
        ("d4+1d4", 6, Mock.RETURN_CONSTANT),
    ],
)
def test_addition(r, out, mock):
    result = roll(r, mock_mode=mock)
    assert result == out


@pytest.mark.parametrize(
    "r,out,mock",
    [
        ("-d40", -3, Mock.RETURN_CONSTANT),
        ("4-3", 1, None),
        ("4--3", 7, None),
        ("---------------4", -4, None),
        ("----------------4", 4, None),
        ("4-2d4", -2, Mock.RETURN_CONSTANT),
        ("2d4-4", 2, Mock.RETURN_CONSTANT),
        ("2d4-d4", 3, Mock.RETURN_CONSTANT),
    ],
)
def test_subtraction(r, out, mock):
    result = roll(r, mock_mode=mock)
    assert result == out


@pytest.mark.parametrize(
    "r,out,mock",
    [
        ("1d4*2", 6, Mock.RETURN_CONSTANT),
        ("(1d4+1d10)*2", 12, Mock.RETURN_CONSTANT),
    ],
)
def test_multiplication(r, out, mock):
    result = roll(r, mock_mode=mock)
    assert result == out


@pytest.mark.parametrize(
    "r,out,mock",
    [
        ("1d4/2", 1, Mock.RETURN_CONSTANT),  # Down
        ("1d4\\2", 2, Mock.RETURN_CONSTANT),  # Up
    ],
)
def test_division(r, out, mock):
    result = roll(r, mock_mode=mock)
    assert result == out


@pytest.mark.parametrize(
    "r,out,mock",
    [
        ("1d4%2", 1, Mock.RETURN_CONSTANT),
        ("1d4%3", 0, Mock.RETURN_CONSTANT),
    ],
)
def test_modulo(r, out, mock):
    result = roll(r, mock_mode=mock)
    assert result == out
