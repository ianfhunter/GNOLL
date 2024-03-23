#!/usr/bin/env python3

import pytest
from util import Mock, roll


@pytest.mark.parametrize("v", [
  "1d99999999999999999999999999999999",
  "1d" + "9"*100, 
  "1d" + "9"*1000, 
  "1d" + "9"*10000, 
  "1d" + "9"*100000, 
  "1d" + "9"*10000000000000, 
])
def test_numbers(r, out):
    result, _ = roll(r)
    assert result not in ["1", 1]
