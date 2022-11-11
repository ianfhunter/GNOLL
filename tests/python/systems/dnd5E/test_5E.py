#!/usr/bin/env python3

from util import roll


def test_5e_roll_for_character_stats():
    # TODO: x6, for all stats
    result, _ = roll("3d6")
    assert result >= 3
    assert result <= 18

    result, _ = roll("4d6kh3")
    assert result >= 3
    assert result <= 18


def test_5e_spell_attack():
    # TODO: Versus DC
    result, _ = roll("1d20+2+4")
    assert result >= 7
    assert result <= 26


def test_5e_roll_hp():
    # TODO: ensure minimum roll of 1

    # Con:5 HitDie:8 Level:2
    result, _ = roll("5+2+d8+2")
    assert result >= 10
    assert result <= 17


def test_5e_halfling_lucky():
    # Note: cannot test intermediate results
    # A possible future feature to consider
    result, _ = roll("d20r==1")
    assert result > 0
    assert result <= 20
