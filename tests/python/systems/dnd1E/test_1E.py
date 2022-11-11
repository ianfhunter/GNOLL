#!/usr/bin/env python3

from util import roll


def test_virtual_dice():
    # roll a d2 using a d6
    result, _ = roll(r"1d6\3")
    assert result >= 1
    assert result <= 2

    # roll a d3 using a d6
    result, _ = roll(r"1d6\2")
    assert result >= 1
    assert result <= 3

    # roll a d10 using a d20
    result, _ = roll(r"1d20\2")
    assert result >= 1
    assert result <= 10
