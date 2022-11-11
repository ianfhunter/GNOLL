#!/usr/bin/env python3

from util import roll


def test_dcc_weird_dice():
    result, _= roll("d3")
    assert result >= 1
    assert result <= 3
    result, _= roll("d5")
    assert result >= 1
    assert result <= 5
    result, _= roll("d12")
    assert result >= 1
    assert result <= 12
    result, _= roll("d18")
    assert result >= 1
    assert result <= 18
    result, _= roll("d24")
    assert result >= 1
    assert result <= 24
    result, _= roll("d30")
    assert result >= 1
    assert result <= 30


def test_dcc_weird_dice_via_other_dice():
    # https://www.reddit.com/r/rpg/comments/79lge5/weird_dice_in_dcc/
    result, _= roll(r"d10\2")
    assert result >= 1
    assert result <= 5
    result, _= roll("d6+(6*z2)")
    assert result >= 1
    assert result <= 12
    result, _= roll("d6+(6*z3)")
    assert result >= 1
    assert result <= 18
    result, _= roll("d6+(6*z4)")
    assert result >= 1
    assert result <= 24
    result, _= roll("d10+10*(z3)")
    assert result >= 1
    assert result <= 30
