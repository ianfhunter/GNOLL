import pytest
import csv
import os
import sys
from util import roll

@pytest.mark.xfail
@pytest.mark.parametrize("r,out",[
    ("4", 4),
])
def test_pip_package(r, out):
    # Don't error during collection
    from dicetower.parser import roll

    # Just Numbers
    result = roll(r)
    assert(result == out)
