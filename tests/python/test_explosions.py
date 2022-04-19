#!/usr/bin/env python3

import pytest
from util import roll, Mock


@pytest.mark.parametrize("r,out",[
    ("d3!", 7),
    ("d5!", 3)
])
def test_explosion(r, out):
    result = roll(r, mock_mode=Mock.RETURN_CONSTANT_TWICE_ELSE_CONSTANT_ONE, mock_const=3)
    assert result == out


@pytest.mark.parametrize("r,out",[
    ("2d3!", 8),   #{3,3},{1,1}
    ("2d5!", 6)    #{3,3}
])
def test_multi_dice_explosion(r, out):
    result = roll(r, mock_mode=Mock.RETURN_CONSTANT_TWICE_ELSE_CONSTANT_ONE, mock_const=3)
    assert result == out
