#!/usr/bin/env python3

import pytest
from util import Mock, roll


@pytest.mark.parametrize("r,out", [("d3!", 7), ("d5!", 3),
                                   ("d5e", 3)])  # {3},{3},{1}
def test_explosion(r, out):
    result = roll(
        r,
        mock_mode=Mock.RETURN_CONSTANT_TWICE_ELSE_CONSTANT_ONE,
        mock_const=3,
        verbose=True,
    )
    assert result == out


@pytest.mark.parametrize("r,out", [("2d3!", 8),
                                   ("2d5!", 6)])  # {3,3},{1,1}  # {3,3}
def test_multi_dice_explosion(r, out):
    result = roll(r,
                  mock_mode=Mock.RETURN_CONSTANT_TWICE_ELSE_CONSTANT_ONE,
                  mock_const=3)
    assert result == out


@pytest.mark.parametrize(
    "r,out",
    [
        ("d3!o", 6),
    ],
)
def test_explosion_only_once(r, out):
    result = roll(r,
                  mock_mode=Mock.RETURN_CONSTANT_TWICE_ELSE_CONSTANT_ONE,
                  mock_const=3)
    assert result == out


@pytest.mark.parametrize(
    "r,out",
    [
        ("d4!p", 10),
    ],
)
def test_explosion_penetrate(r, out):
    result = roll(r, mock_mode=Mock.RETURN_DECREMENTING, mock_const=4)
    assert result == out


if __name__ == "__main__":
    test_explosion("d3!", 7)
