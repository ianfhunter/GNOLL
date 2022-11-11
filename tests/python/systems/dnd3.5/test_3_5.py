#!/usr/bin/env python3

from util import roll


def test_3_5_age():
    # Age for an old Gnome
    result, _= roll("150+3d%")
    assert result >= 153
    assert result <= 450


def test_3_5_height():
    # Height for a female Gnome
    result, _= roll("34+2d4")
    assert result >= 36
    assert result <= 42


def test_3_5_weight():
    # Weight for a female Gnome
    result, _= roll("40*1")
    assert result == 40

    # Weight for a male half-elf
    result, _= roll("100*2d4")
    assert result >= 200
    assert result <= 800


def test_3_5_fall_dmg():
    # Weight for a female Gnome
    result, _= roll("20d6")
    assert result >= 20
    assert result <= 120
