#!/usr/bin/env python3

import pytest
from util import roll, Mock

def test_D6():
    r = "d6"
    result = roll(r, mock_mode=Mock.RETURN_CONSTANT, mock_const=3)
    assert result == 3

def test_D66():
    r = "#DSIXTYSIX=(d6*10)+d6;@DSIXTYSIX"
    result = roll(r, mock_mode=Mock.RETURN_CONSTANT, mock_const=3)
    assert result == 33

def test_D666():
    r = "#DSIXSIXSIX=(d6*100)+(d6*10)+d6;@DSIXTYSIX"
    result = roll(r, mock_mode=Mock.RETURN_CONSTANT, mock_const=3)
    assert result == 333
