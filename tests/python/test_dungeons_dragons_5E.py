#!/usr/bin/env python3

import pytest
from util import roll, Mock

def test_5e_roll_for_character_stats():
    result = roll("4d6kh3")
    assert result >= 3
    assert result <= 18

#Todo x6, for all stats 
