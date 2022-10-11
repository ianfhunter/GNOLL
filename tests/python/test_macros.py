#!/usr/bin/env python3

import os
import pytest
from util import Mock, roll

@pytest.mark.parametrize("r,out,mock",[
    ("#MY_DIE=d{A};d4", 3, Mock.RETURN_CONSTANT),
    ("#MY_DIE=d{A};2d4", 6, Mock.RETURN_CONSTANT)
])
def test_macro_storage(r, out, mock):
    result = roll(r, mock_mode=mock)
    assert result == out

@pytest.mark.parametrize("r,out,mock",[
    ("#MY_DIE=d{A};@MY_DIE", "A", Mock.NO_MOCK)
])
def test_macro_usage(r, out, mock):
    result = roll(r, mock_mode=mock)
    assert result == out

def test_D66():
    r = "#DSIXTYSIX=(d6*10)+d6;@DSIXTYSIX"
    result = roll(r, mock_mode=Mock.RETURN_CONSTANT, mock_const=3)
    assert result == 33

def test_builtins():
    # Check that builtins are valid calls
    d = os.path.join(,"../../builtins/*.dice)
    for name in glob.glob(d):
       with open(name) as f:
           for macro in f.readlines():
              print("Macro:", name)
              roll(macro)
