import pytest
import csv
import os
import sys
from util import roll

def test_pip_package():
    from dicetower.parser import roll

    err_code, result = roll("1d4")
    assert(err_code == 0)
    assert(result in [1,2,3,4])
