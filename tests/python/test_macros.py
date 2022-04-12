#!/usr/bin/env python3

from unittest import mock
import pytest
import csv
import os
import sys
from util import roll, Mock

@pytest.mark.parametrize("r,out,mock",[
    ("#MY_DIE=d{A};d4", 3, Mock.RETURN_CONSTANT)
])
def test_macro_storage(r, out, mock):
    result = roll(r, mock_mode=mock)
    assert(result == out)

@pytest.mark.skip()
@pytest.mark.parametrize("r,out,mock",[
    ("#MY_DIE=d{A};@MY_DIE", "A", Mock.NO_MOCK)
])
def test_macro_usage(r, out, mock):
    result = roll(r, mock_mode=mock)
    assert(result == out)
