#!/usr/bin/env python3

import pytest
from util import Mock, roll

# TODO: better tests for percentage dice - not fool proof


def test_percentile_dice():
    result = roll("d%")
    assert result > 0
    assert result <= 100

def test_coin_as_dice():
    result = roll("dc")
    assert result > 0
    assert result <= 2


def test_percentile_dice_with_modulo():
    result = roll("d%%2")
    assert result >= 0
    assert result < 2


def test_multi_percentile_dice():
    result = roll("2d%")
    assert result > 2
    assert result <= 200


def test_negative_percentile_dice():
    result = roll("-d%")
    assert result < 0
    assert result >= -100
