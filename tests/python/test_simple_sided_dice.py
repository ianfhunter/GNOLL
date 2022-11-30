#!/usr/bin/env python3

import pytest
from util import Mock, error_handled_by_gnoll, roll


def test_random_roll():
    # Prove Random roll Is Working
    a = b = c = d = False
    for _ in range(100):
        result, _ = roll("d4")

        assert result > 0
        assert result < 5
        if result == 1:
            a = True
        if result == 2:
            b = True
        if result == 3:
            c = True
        if result == 4:
            d = True
        if a and b and c and d:
            break
    assert a
    assert b
    assert c
    assert d


def test_random_roll_zeros():
    # Prove Random roll Is Working
    a = b = c = d = False
    for _ in range(100):
        result, _ = roll("z4")

        assert result > -1
        assert result < 4
        if result == 0:
            a = True
        if result == 1:
            b = True
        if result == 2:
            c = True
        if result == 3:
            d = True
        if a and b and c and d:
            break
    assert a
    assert b
    assert c
    assert d


def test_space_removal():
    result, _ = roll("   d    4   ")
    assert result > 0
    assert result < 5


def test_negative_roll():
    result, _ = roll("-d4")
    assert result > -5
    assert result < 0


def test_non_rolling_roll():
    result, _ = roll("d0")
    assert result == 0
    result, _ = roll("d1")
    assert result == 1
    result, _ = roll("-d0")
    assert result == 0
    result, _ = roll("0d4")
    assert result == 0


@pytest.mark.parametrize(
    "r", [("d"), ("d2d"), ("2d2d2"), ("2d2d2d"), ("1d"), ("d-1"), ("-1d-1")]
)
def test_bad_simple_rolls(r):
    try:
        roll(r)
    except Exception as e:
        error_handled_by_gnoll(e)


def test_dice_numbers():
    result, _ = roll("2d6", mock_mode=Mock.RETURN_CONSTANT)
    assert result == 6


def test_distinct_dice():
    result, _ = roll("d6;d6", mock_mode=Mock.RETURN_CONSTANT, mock_const=2)
    assert result == [2, 2]
