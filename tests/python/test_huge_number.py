#!/usr/bin/env python3

import pytest
from util import roll


@pytest.mark.parametrize(
    "r, at_least",
    [("1d922337203685477580", 10000000000000000)],
)
def test_longlong(r, at_least):
    largest_value = 0
    for _ in range(300):
        result, _ = roll(r)
        largest_value = max(largest_value, result)
        if largest_value > at_least:
            break
    assert largest_value > at_least


@pytest.mark.skip(reason="Not Implemented yet")
@pytest.mark.parametrize(
    "r, at_least",
    [
        ("1d" + "9" * 100, int("1" * 100)),
        ("1d" + "9" * 1000, int("1" * 1000)),
        # Numbers larger than this start causing issues in python even if we dont run the test.
    ],
)
def test_ridiculously_big_numbers(r, at_least):
    largest_value = 0
    for _ in range(300):
        result, _ = roll(r)
        largest_value = max(largest_value, result)
        if largest_value > at_least:
            break
    assert largest_value > at_least
