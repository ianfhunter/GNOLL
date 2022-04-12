#!/usr/bin/env python3

from unittest import mock
import pytest
import csv
import os
import sys
from util import roll, Mock

@pytest.mark.parametrize("r,out,mock",[
    ("d{A}", "A", Mock.NO_MOCK),
    ("d{A,B,C,D}", "D", Mock.RETURN_CONSTANT)
])
def test_symbolic_dice(r, out, mock):
    result = roll(r, mock_mode=mock)
    assert(result == out)

@pytest.mark.skip()
@pytest.mark.parametrize("r,out,mock",[
    ("2d{A,B,C,D}", "DD", Mock.RETURN_CONSTANT)
])
def test_multiple_symbolic_dice(r, out, mock):
    result = roll(r, mock_mode=mock)
    assert(result == out)

@pytest.mark.parametrize("r,out,mock",[
    ("d{HEARTS,SPADES,CLUBS,DIAMONDS}", "DIAMONDS", Mock.RETURN_CONSTANT)
])
def test_long_string(r, out, mock):
    result = roll(r, mock_mode=mock)
    assert(result == out)
