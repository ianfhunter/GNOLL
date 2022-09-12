#!/usr/bin/env python3

import pytest
from util import roll, Mock

def test_5e_roll_for_character_stats():
    # TODO: x6, for all stats
    result = roll("3d6")
    assert result >= 3
    assert result <= 18

    result = roll("4d6kh3")
    assert result >= 3
    assert result <= 18
    
def test_5e_spell_attack():
    # TODO: Versus DC
    result = roll("1d20+2+4")
    assert result >= 7
    assert result <= 26

def test_5e_roll_hp():
    # TODO: ensure minimum roll of 1
    
    # Con:5 HitDie:8 Level:2
    result = roll("5+2+d8+2")
    assert result >= 10
    assert result <= 17

