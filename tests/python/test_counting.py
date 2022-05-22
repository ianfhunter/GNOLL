#!/usr/bin/env python3

import pytest
from util import roll, Mock


@pytest.mark.parametrize("r,out,mock,mock_const",[
    ("10d10c>5", 5, Mock.RETURN_INCREMENTING, 1),
])
def test_count(r, out, mock, mock_const):
    result = roll(r, mock_mode=mock, mock_const=mock_const)
    assert result == out

# TODO: vectors?