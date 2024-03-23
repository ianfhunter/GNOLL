#!/usr/bin/env python3

import pytest
from util import Mock, error_handled_by_gnoll, roll


@pytest.mark.parametrize(
    "r,out,mock,mock_const",
    [
        ("2d20kh", 2, Mock.RETURN_INCREMENTING, 1),
        ("2d20dl", 2, Mock.RETURN_INCREMENTING, 1),
        # ("2d20h",  2, Mock.RETURN_INCREMENTING, 1)
    ],
)
def test_keepdrop_highest(r, out, mock, mock_const):
    result, _ = roll(r, mock_mode=mock, mock_const=mock_const)
    assert result == out


@pytest.mark.parametrize(
    "r,out,mock,mock_const",
    [
        ("2d20kl", 1, Mock.RETURN_INCREMENTING, 1),
        ("2d20dh", 1, Mock.RETURN_INCREMENTING, 1),
        # ("2d20l",  1, Mock.RETURN_INCREMENTING, 1),
    ],
)
def test_keepdrop_lowest(r, out, mock, mock_const):
    result, _ = roll(r, mock_mode=mock, mock_const=mock_const)
    assert result == out


@pytest.mark.parametrize(
    "r,out,mock,mock_const",
    [
        ("3d20kh2", 5, Mock.RETURN_INCREMENTING, 1),
        ("3d20kl2", 3, Mock.RETURN_INCREMENTING, 1),
        ("3d20dh2", 1, Mock.RETURN_INCREMENTING, 1),
        ("3d20dl2", 3, Mock.RETURN_INCREMENTING, 1),
    ],
)
def test_keepdrop_multiple(r, out, mock, mock_const):
    result, _ = roll(r, mock_mode=mock, mock_const=mock_const)
    assert result == out


@pytest.mark.parametrize(
    "r,out,mock,mock_const",
    [
        ("3d20dhdl", 2, Mock.RETURN_INCREMENTING, 1),
    ],
)
def test_middle(r, out, mock, mock_const):
    result, _ = roll(r, mock_mode=mock, mock_const=mock_const)
    assert result == out


@pytest.mark.parametrize("r", ["1d6kh2"])
def test_keepdrop_redundant(r):
    """
    Tests the case where "kh" or similar is not needed because the dice pool is already that small.
    """
    try:
        roll(r)
    except Exception as e:
        error_handled_by_gnoll(e)
