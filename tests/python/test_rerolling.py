#!/usr/bin/env python3

import pytest
from util import roll, Mock


# @pytest.mark.skip()
@pytest.mark.parametrize("r,out,mock,mock_const",[
    ("d4r==1", 2, Mock.RETURN_INCREMENTING, 1),
])
def test_rerolling(r, out, mock, mock_const):
    result = roll(r, mock_mode=mock, mock_const=mock_const)
    assert result == out
