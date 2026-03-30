#!/usr/bin/env python3

import os

import pytest

from gnoll import GNOLLException, roll
from gnoll.validation import (
    _MAX_DECIMAL_TOKEN_LEN,
    _MAX_DICE_PER_ROLL,
    validate_roll_string,
)

_DICE_SO = os.path.join(
    os.path.dirname(__file__),
    "../../src/python/code/gnoll/c_build/dice.so",
)


def test_huge_decimal_literal_rejected():
    s = "9" * 100 + "d6"
    with pytest.raises(GNOLLException) as exc:
        validate_roll_string(s)
    assert "OUT_OF_RANGE" in str(exc.value)


def test_decimal_token_length_boundary():
    """Max-length digit run is allowed when the parsed value fits in LLONG_MAX."""
    ok_len = "0" * _MAX_DECIMAL_TOKEN_LEN
    validate_roll_string(ok_len + "+1")

    too_long = "1" * (_MAX_DECIMAL_TOKEN_LEN + 1)
    with pytest.raises(GNOLLException) as exc:
        validate_roll_string(too_long + "+0")
    assert "OUT_OF_RANGE" in str(exc.value)


def test_extreme_dice_count_rejected():
    with pytest.raises(GNOLLException) as exc:
        validate_roll_string("999999999d999999999")
    assert "MAX_LOOP_LIMIT_HIT" in str(exc.value)


def test_dice_count_just_over_cap_rejected():
    with pytest.raises(GNOLLException) as exc:
        validate_roll_string(f"{_MAX_DICE_PER_ROLL + 1}d6")
    assert "MAX_LOOP_LIMIT_HIT" in str(exc.value)


def test_dice_count_at_cap_passes_validation():
    validate_roll_string(f"{_MAX_DICE_PER_ROLL}d6")


def test_implicit_single_die_passes_validation():
    validate_roll_string("d20")


def test_roll_applies_validation_before_native():
    with pytest.raises(GNOLLException):
        roll("9" * 100 + "d6", breakdown=False)


@pytest.mark.skipif(not os.path.isfile(_DICE_SO), reason="Native dice.so not built")
def test_normal_roll_still_works():
    code, result, _ = roll("2d6", breakdown=False)
    assert code == 0
    assert isinstance(result, list)


@pytest.mark.skipif(not os.path.isfile(_DICE_SO), reason="Native dice.so not built")
def test_native_rejects_dice_count_over_cap(monkeypatch):
    """Exercise C GNOLL_MAX_DICE_PER_ROLL when Python validation is bypassed."""
    monkeypatch.setattr("gnoll.validation.validate_roll_string", lambda _s: None)
    with pytest.raises(GNOLLException) as exc:
        roll(f"{_MAX_DICE_PER_ROLL + 1}d6", breakdown=False)
    assert "MAX_LOOP_LIMIT_HIT" in str(exc.value)


@pytest.mark.skipif(not os.path.isfile(_DICE_SO), reason="Native dice.so not built")
def test_native_rejects_oversized_number_token(monkeypatch):
    monkeypatch.setattr("gnoll.validation.validate_roll_string", lambda _s: None)
    with pytest.raises(GNOLLException) as exc:
        roll("1" * (_MAX_DECIMAL_TOKEN_LEN + 1) + "d6", breakdown=False)
    assert "OUT_OF_RANGE" in str(exc.value)
