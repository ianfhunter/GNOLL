#!/usr/bin/env python3

import pytest
from util import Mock, roll


def test_d6():
    r = "d6"
    result, _ = roll(r, mock_mode=Mock.RETURN_CONSTANT, mock_const=3)
    assert result == 3


@pytest.mark.skip("Macros currently not supporting Operation Storage")
def test_d66():
    r = "#DSIXTYSIX=(d6*10)+d6;@DSIXTYSIX"
    result, _ = roll(r, mock_mode=Mock.RETURN_CONSTANT, mock_const=3)
    assert result == 33


@pytest.mark.skip("Macros currently not supporting Operation Storage")
def test_d666():
    r = "#DSIXSIXSIX=(d6*100)+(d6*10)+d6;@DSIXTYSIX"
    result, _ = roll(r, mock_mode=Mock.RETURN_CONSTANT, mock_const=3)
    assert result == 333
