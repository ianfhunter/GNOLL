#!/usr/bin/env python3

import pytest
from util import roll, Mock

def test_bw_dsix_over_four():
    # TODO: x6, for all stats
    result = roll("6d6f>=4c")
    assert result >= 1
    assert result <= 6
