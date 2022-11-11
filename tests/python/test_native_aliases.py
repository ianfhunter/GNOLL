#!/usr/bin/env python3

from util import roll


def test_percentile_dice():
    result, _ = roll("d%")
    assert result > 0
    assert result <= 100


def test_coin_as_dice():
    result, _ = roll("dc")
    assert result > 0
    assert result <= 2


def test_percentile_dice_with_modulo():
    result, _ = roll("d%%2")
    assert result >= 0
    assert result < 2


def test_multi_percentile_dice():
    result, _ = roll("2d%")
    assert result > 2
    assert result <= 200


def test_negative_percentile_dice():
    result, _ = roll("-d%")
    assert result < 0
    assert result >= -100
