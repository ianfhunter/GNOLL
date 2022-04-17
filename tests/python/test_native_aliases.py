#!/usr/bin/env python3

import pytest
from util import roll, Mock

# TODO: better tests for percentage dice - not fool proof


def test_percentile_dice():
    result = roll("d%")
    assert result > 0
    assert result < 100


def test_percentile_dice():
    result = roll("d%%2")
    assert result >= 0
    assert result < 2
