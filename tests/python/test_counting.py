#!/usr/bin/env python3

import pytest
from util import Mock, roll


@pytest.mark.parametrize("r,out,mock,mock_const",[
    ("10d10c", 10, Mock.RETURN_INCREMENTING, 1),
    ("10d10f>5c", 5, Mock.RETURN_INCREMENTING, 1),
])
def test_count(r, out, mock, mock_const):
    result = roll(r, mock_mode=mock, mock_const=mock_const)
    assert result == out


@pytest.mark.parametrize("r,out,mock,mock_const",[
    ("4d10uc", 4, Mock.RETURN_INCREMENTING, 1),
])
def test_count_unique(r, out, mock, mock_const):
    result = roll(r, mock_mode=mock, mock_const=mock_const)
    assert result == out
