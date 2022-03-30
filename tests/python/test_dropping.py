#!/usr/bin/env python3

from unittest import mock
import pytest
import csv
import os
import sys
from util import roll


@pytest.mark.parametrize("r,out,mock",[
    # Test each type of notation
    ## Keep Highest
    ("2d20kh", 11, (8,11)),
    ("2d20dl", 11, (8,11)),
    ("2d20h", 11, (8,11)),
    ## Keep Lowest
    ("2d20kl", 8, (8,11)),
    ("2d20dh", 8, (8,11)),
    ("2d20l", 8, (8,11)),
    # Keep >1
    ("3d20kh2", 30, (8,11, 19)),
    ("3d20kl2", 18, (8,10, 19)),
])

def test_dropping(r, out, mock):
    result = roll(r, mock_random=mock)
    assert(result == out)