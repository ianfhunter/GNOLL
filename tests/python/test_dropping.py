#!/usr/bin/env python3

import pytest
from util import roll, Mock


@pytest.mark.parametrize("r,out,mock",[
    # Test each type of notation
    ## Keep Highest
    ("2d20kh", 2, Mock.RETURN_INCREMENTING),
    ("2d20dl", 2, Mock.RETURN_INCREMENTING),
    ("2d20h",  2, Mock.RETURN_INCREMENTING),
    ## Keep Lowest
    ("2d20kl", 1, Mock.RETURN_INCREMENTING),
    ("2d20dh", 1, Mock.RETURN_INCREMENTING),
    ("2d20l",  1, Mock.RETURN_INCREMENTING),
    # Keep >1
    ("3d20kh2", 5, Mock.RETURN_INCREMENTING),
    ("3d20kl2", 3, Mock.RETURN_INCREMENTING),
])
def test_dropping(r, out, mock):
    result = roll(r, mock_mode=mock)
    assert result == out
