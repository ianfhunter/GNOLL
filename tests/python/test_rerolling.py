#!/usr/bin/env python3

import pytest
from util import roll, Mock


@pytest.mark.skip()
@pytest.mark.parametrize("r,out",[
    ("d4r==3", 4),
])
def test_numbers(r, out):
    # Just Numbers
    result = roll(r)
    assert result == out
