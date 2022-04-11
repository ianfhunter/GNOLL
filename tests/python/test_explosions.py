#!/usr/bin/env python3

from unittest import mock
import pytest
import csv
import os
import sys
from util import roll, Mock

@pytest.mark.parametrize("r,out",[
    ("d3!", 7),
    ("d5!", 3)
])
def test_explosion(r, out):
    result = roll(r, mock_mode=Mock.RETURN_CONSTANT_TWICE_ELSE_CONSTANT_ONE, mock_const=3)
    assert(result == out)
