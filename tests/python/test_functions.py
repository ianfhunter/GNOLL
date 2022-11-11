#!/usr/bin/env python3

import pytest
from util import Mock, roll


@pytest.mark.parametrize(
    "dice, expected_result",
    [
        ("max(1,2)", 2),
        ("max(4,3)", 4),
        ("min(1,2)", 1),
        ("min(4,3)", 3),
        ("abs(10)", 10),
        ("abs(-11)", 11),
    ],
)
def test_functions(dice, expected_result):
    result, _ = roll(dice, mock_mode=Mock.RETURN_CONSTANT, mock_const=0)
    assert result == expected_result
