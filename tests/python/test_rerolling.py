#!/usr/bin/env python3

import pytest
from util import roll, Mock


@pytest.mark.parametrize("r,out,mock,mock_const",[
    ("d4r==1", 2, Mock.RETURN_INCREMENTING, 1),
    # ("d4r<=1", 2, Mock.RETURN_INCREMENTING, 1),
    # ("d4r>1", 1, Mock.RETURN_INCREMENTING, 1),
])
def test_rerolling(r, out, mock, mock_const):
    result = roll(r, mock_mode=mock, mock_const=mock_const)
    assert result == out

# @pytest.mark.parametrize("r,out,mock,mock_const",[
#     ("2d4r==1", 2, Mock.RETURN_INCREMENTING, 1),
# ])
# def test_rerolling_multidice(r, out, mock, mock_const):
#     result = roll(r, mock_mode=mock, mock_const=mock_const)
#     assert result == out

# @pytest.mark.parametrize("r,out,mock,mock_const",[
#     ("d4!r==9", 6, Mock.RETURN_INCREMENTING, 4),
#     # {4, !+5=9, r6}
# ])
# def test_rerolling_explosion(r, out, mock, mock_const):
#     result = roll(r, mock_mode=mock, mock_const=mock_const)
#     assert result == out


# @pytest.mark.parametrize("r,out,mock,mock_const",[
#     ("2d20khr==2", 3, Mock.RETURN_INCREMENTING, 1),
# ])
# def test_rerolling_dropping(r, out, mock, mock_const):
#     result = roll(r, mock_mode=mock, mock_const=mock_const)
#     assert result == out
