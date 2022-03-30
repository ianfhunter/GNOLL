import pytest
import csv
import os
import sys
from util import roll
from dicetower.parser import roll

@pytest.mark.parametrize("r,out",[
    ("4", 4),
])
def test_pip_package(r, out):
    # Just Numbers
    result = roll(r)
    assert(result == out)
