#!/usr/bin/env python3

import pytest
from util import roll


@pytest.mark.parametrize(
    "r, at_least",
    [
        ("1d922337203685477580", 10000000000000000)
        # "1d" + "9" * 100,    # Too large for long long
        # "1d" + "9" * 1000,
        # "1d" + "9" * 10000,
        # "1d" + "9" * 100000,
        # "1d" + "9" * 10000000000000, # Too large for Python :)
    ],
)
def test_numbers(r, at_least):
    largest_value = 0
    for x in range(300):
        result, _ = roll(r)
        largest_value = max(largest_value, result)
        if largest_value > at_least:
            break
    assert largest_value > at_least
