#!/usr/bin/env python3

import pytest
from util import roll, Mock

def test_ranges():
    result = roll("d{10..40}")
    print(result)
    assert result >= 10
    assert result <= 40

@pytest.mark.skip()
def test_multiple_ranges():
    result = roll("2d{10..15}")
    print(result)
    assert result >= 20
    assert result <= 30
