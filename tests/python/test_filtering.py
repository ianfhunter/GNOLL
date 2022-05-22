#!/usr/bin/env python3

import pytest
from util import roll, Mock


@pytest.mark.parametrize("r,out,mock,mock_const",[
    ("10d10f<4", 6, Mock.RETURN_INCREMENTING, 1),
    ("10d10f>8", 19, Mock.RETURN_INCREMENTING, 1),
])
def test_filter(r, out, mock, mock_const):
    result = roll(r, mock_mode=mock, mock_const=mock_const)
    assert result == out

