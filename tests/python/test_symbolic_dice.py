#!/usr/bin/env python3

import pytest
from util import Mock, roll


@pytest.mark.parametrize(
    "r,out,mock",
    [
        ("d{A}", "A", Mock.NO_MOCK),
        # ("d{A,B,C,D}", "D", Mock.RETURN_CONSTANT)
    ],
)
def test_symbolic_dice(r, out, mock):
    result = roll(r, mock_mode=mock)
    assert result == out


@pytest.mark.parametrize("r,out,mock",
                         [("2d{A,B,C,D}", ["D", "D"], Mock.RETURN_CONSTANT)])
def test_multiple_symbolic_dice(r, out, mock):
    result = roll(r, mock_mode=mock)
    assert result == out


@pytest.mark.parametrize(
    "r,out,mock",
    [
        ("d{HEARTS,SPADES,CLUBS,DIAMONDS}", "DIAMONDS", Mock.RETURN_CONSTANT),
        # Star Wars FFG
        (
            "d{DARKSIDE, DARKSIDE, DARKSIDE, DARKSIDE, DARKSIDE, DARKSIDE, DARKSIDE_DARKSIDE, LIGHTSIDE, LIGHTSIDE, LIGHTSIDE_LIGHTSIDE, LIGHTSIDE_LIGHTSIDE, LIGHTSIDE_LIGHTSIDE}",
            "DARKSIDE",
            Mock.RETURN_CONSTANT,
        ),
    ],
)
def test_long_string(r, out, mock):
    result = roll(r, mock_mode=mock)
    assert result == out


pytest.mark.parametrize("r,out,mock",
                        [("2d{2,2,2,2,3}", 2, Mock.RETURN_CONSTANT)])
def test_multiple_numeric_dice(r, out, mock):
    result = roll(r, mock_mode=mock)
    assert result == out
