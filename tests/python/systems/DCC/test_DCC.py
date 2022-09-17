#!/usr/bin/env python3

import pytest
from util import roll, Mock



def test_dcc_weird_dice():
    result = roll("d3")
    assert result >= 1
    assert result <= 3
