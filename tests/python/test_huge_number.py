#!/usr/bin/env python3

import pytest
from util import roll


@pytest.mark.parametrize(
    "r",
    [
        "1d99999999999999999999999999999999",
        "1d" + "9" * 100,
        "1d" + "9" * 1000,
        "1d" + "9" * 10000,
        "1d" + "9" * 100000,
        # "1d" + "9" * 10000000000000, # Too large for Python :)
    ],
)
def test_numbers(r):
    result, _ = roll(r)
    assert result not in ["1", 1]
