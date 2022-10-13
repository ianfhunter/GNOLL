#!/usr/bin/env python3

import pytest
from util import Mock, roll


@pytest.mark.parametrize("r,out,mock,mock_const",[
    ("d4r==1", 2, Mock.RETURN_INCREMENTING, 1),
    ("d4r<=1", 2, Mock.RETURN_INCREMENTING, 1),
    ("d4r<2", 2, Mock.RETURN_INCREMENTING, 1),
    ("d4r>=1", 2, Mock.RETURN_INCREMENTING, 1),
    ("d4r>1", 1, Mock.RETURN_INCREMENTING, 1),
    ("d4r!=1", 1, Mock.RETURN_INCREMENTING, 1),
    ("d4r!=4", 2, Mock.RETURN_INCREMENTING, 1),
])
def test_rerolling(r, out, mock, mock_const):
    result = roll(r, mock_mode=mock, mock_const=mock_const)
    assert result == out

@pytest.mark.parametrize("r,out,mock,mock_const",[
    ("2d4r==1", 3, Mock.RETURN_INCREMENTING, 1),
    ("2d4r==3", 7, Mock.RETURN_INCREMENTING, 1),
])
def test_rerolling_multidice(r, out, mock, mock_const):
    result = roll(r, mock_mode=mock, mock_const=mock_const)
    assert result == out

@pytest.mark.parametrize("r,out,mock,mock_const",[
    ("d4!r==9", 6, Mock.RETURN_INCREMENTING, 4),
])
def test_rerolling_explosion(r, out, mock, mock_const):
    result = roll(r, mock_mode=mock, mock_const=mock_const)
    assert result == out

# Skipped Tests Below This Line

@pytest.mark.skip()
@pytest.mark.parametrize("r,out,mock,mock_const",[
    ("2d20khr==2", 3, Mock.RETURN_INCREMENTING, 1),
])
def test_reroll_dropkeep_until(r, out, mock, mock_const):
    result = roll(r, mock_mode=mock, mock_const=mock_const)
    assert result == out

@pytest.mark.skip()
@pytest.mark.parametrize("r,out,mock,mock_const",[
    ("2d20khr==2", 3, Mock.RETURN_INCREMENTING, 1),
])
def test_rerolling_dropping(r, out, mock, mock_const):
    result = roll(r, mock_mode=mock, mock_const=mock_const)
    assert result == out

@pytest.mark.parametrize("r,out,mock,mock_const",[
    ("d10rr>4", 5, Mock.RETURN_INCREMENTING, 1),
])
def test_reroll_until(r, out, mock, mock_const):
    result = roll(r, mock_mode=mock, mock_const=mock_const)
    assert result == out

