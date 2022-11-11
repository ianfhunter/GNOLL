#!/usr/bin/env python3

import pytest
from util import Mock, roll


def test_breakdown():
    # Just Numbers
    result, breakdown = roll("200d20")
    breakdown = breakdown[0]
    print(breakdown)
    assert all([b > 0 for b in breakdown])
    assert all([b <= 20 for b in breakdown])
    assert result > 200
    assert result <= 200 * 20
