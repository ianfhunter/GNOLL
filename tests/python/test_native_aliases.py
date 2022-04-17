#!/usr/bin/env python3

import pytest
from util import roll, Mock

# TODO: better tests for percentage dice - not fool proof


def test_percentile_dice():
    result = roll("d%")
    assert result > 0
    assert result <= 100


def test_percentile_dice_with_modulo():
    result = roll("d%%2")
    assert result >= 0
    assert result < 2


@pytest.mark.xfail
def test_multi_percentile_dice():
    result = roll("2d%")
    assert result > 0
    assert result <= 100


def test_negative_percentile_dice():
    result = roll("-d%")
    assert result < 0
    assert result >= -100
