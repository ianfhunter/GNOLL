#!/usr/bin/env python3

import pytest
from util import Mock, roll

@pytest.mark.parametrize("r,out,mock,mock_const",[
    ("2d2d2d==1", 3, Mock.RETURN_INCREMENTING, 1),
])
def test_rerolling_multidice(r, out, mock, mock_const):
    with pytest.raises(Exception):
        result = roll(r, mock_mode=mock, mock_const=mock_const)
        assert result == out
