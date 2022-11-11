#!/usr/bin/env python3

import pytest
from util import roll


def test_ranges():
    result, _= roll("d{10..40}")
    assert result >= 10
    assert result <= 40


@pytest.mark.skip("not implemented")
def test_multiple_ranges():
    result, _= roll("2d{10..15}")
    assert result >= 20
    assert result <= 30
