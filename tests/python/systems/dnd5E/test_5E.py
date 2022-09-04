#!/usr/bin/env python3

import pytest
from util import roll, Mock

def test_5e_roll_for_character_stats():
    # TODO: x6, for all stats
    result = roll("4d6kh3")
    assert result >= 3
    assert result <= 18

def test_spell_attack():
    # TODO: Versus DC
    result = roll("1d20+2+4")
    assert result >= 7
    assert result <= 26
