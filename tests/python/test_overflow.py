#!/usr/bin/env python3

import pytest
from util import Mock, roll


@pytest.mark.parametrize("r",[
    ("2147483647+2147483647"),
    ("-2147483647-2147483647"),
    ("2147483645+2147483644"),
    ("-2147483640*2"),
    ("10000d214748364")
])
def test_modulo(r):
    try:
        roll(r)
    except Exception as e:
        error_handled_by_gnoll(e)
