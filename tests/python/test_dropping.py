#!/usr/bin/env python3

import pytest
from util import roll, Mock


@pytest.mark.parametrize("r,out,mock,mock_const",[
    ("2d20kh", 2, Mock.RETURN_INCREMENTING, 1),
    ("2d20dl", 2, Mock.RETURN_INCREMENTING, 1),
    ("2d20h",  2, Mock.RETURN_INCREMENTING, 1)
])
def test_drop_highest(r, out, mock, mock_const):
    result = roll(r, mock_mode=mock, mock_const=mock_const)
    assert result == out


@pytest.mark.parametrize("r,out,mock,mock_const",[
    ("2d20kl", 1, Mock.RETURN_INCREMENTING, 1),
    ("2d20dh", 1, Mock.RETURN_INCREMENTING, 1),
    ("2d20l",  1, Mock.RETURN_INCREMENTING, 1),
])
def test_drop_lowest(r, out, mock, mock_const):
    result = roll(r, mock_mode=mock, mock_const=mock_const)
    assert result == out


@pytest.mark.parametrize("r,out,mock,mock_const",[
    ("3d20kh2", 5, Mock.RETURN_INCREMENTING, 1),
    ("3d20kl2", 3, Mock.RETURN_INCREMENTING, 1),
])
def test_drop_multiple(r, out, mock, mock_const):
    result = roll(r, mock_mode=mock, mock_const=mock_const)
    assert result == out
