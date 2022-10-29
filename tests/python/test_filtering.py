#!/usr/bin/env python3

import pytest
from util import Mock, roll


@pytest.mark.parametrize(
    "r,out,mock,mock_const",
    [
        ("10d10f<4", 6, Mock.RETURN_INCREMENTING, 1),  # less than
        ("10d10f>8", 19, Mock.RETURN_INCREMENTING, 1),  # greater than
        ("10d10f!=1", 54, Mock.RETURN_INCREMENTING, 1),  # is not
        ("10d10f==1", 1, Mock.RETURN_INCREMENTING, 1),  # is equal
        ("10d10f>=8", 27, Mock.RETURN_INCREMENTING,
         1),  # equal or greater than
        ("10d10f<=3", 6, Mock.RETURN_INCREMENTING, 1),  # equal or less than
        ("10d10fis_even", 5, Mock.RETURN_INCREMENTING, 1),  # even
        ("10d10fis_odd", 5, Mock.RETURN_INCREMENTING, 1),  # odd
        ("10d10fis_same", 0, Mock.RETURN_INCREMENTING, 1),  # same
    ],
)
def test_filter(r, out, mock, mock_const):

    # https://github.com/ianfhunter/GNOLL/issues/216
    result = roll(r, mock_mode=mock, mock_const=mock_const)
    assert result == out
