#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from util import roll


def test_bw_dsix_over_four():
    # TODO: x6, for all stats
    result, _ = roll("6d6f>=4c")
    assert result >= 0
    assert result <= 6
