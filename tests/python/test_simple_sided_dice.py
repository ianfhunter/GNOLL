#!/usr/bin/env python3

import pytest
from util import roll, Mock

def test_random_roll():
    # Prove Random roll Is Working
    a = b = c = d = False
    for x in range(100):
        result = roll("d4")
        
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
        if (a and b and c and d):
            break
    assert a
    assert b
    assert c
    assert d

def test_space_removal():
    result = roll("   d    4   ")
    assert result > 0
    assert result < 5

def test_negative_roll():
    result = roll("-d4")
    assert result > -5
    assert result < 0

def test_non_rolling_roll():
    result = roll("d0")
    assert result == 0
    result = roll("d1")
    assert result == 1
    result = roll("-d0")
    assert result == 0
    result = roll("0d4")
    assert result == 0

def test_bad_simple_rolls():
    with pytest.raises(Exception):
        # Just "Dice" does not make sense
        roll("d")
    with pytest.raises(Exception):
        # Just "Dice" does not make sense
        roll("d2d")
    with pytest.raises(Exception):
        # See above
        roll("1d")
    with pytest.raises(Exception):
        # Negative Sides does not make sense
        roll("d-1")
    with pytest.raises(Exception):
        # Negative Sides does not make sense
        roll("-1d-1")

def test_dice_numbers():
    result = roll("2d6", mock_mode=Mock.RETURN_CONSTANT)
    assert result == 6

@pytest.mark.skip()
def test_multi_d_numbers():
    result = roll("3d3d3", mock_mode=Mock.RETURN_CONSTANT, mock_const=2)
    # 2d3 -> 2,2 -> 4
    assert result == 4

def test_distinct_dice():
    result = roll("d6;d6", mock_mode=Mock.RETURN_CONSTANT, mock_const=2)
    assert result == [2,2]
