#!/usr/bin/env python3

import os

import pytest

from gnoll import GNOLLException
from gnoll.validation import validate_roll_string


def test_huge_decimal_literal_rejected():
    s = "9" * 100 + "d6"
    with pytest.raises(GNOLLException) as exc:
        validate_roll_string(s)
    assert "OUT_OF_RANGE" in str(exc.value)


def test_extreme_dice_count_rejected():
    with pytest.raises(GNOLLException) as exc:
        validate_roll_string("999999999d999999999")
    assert "MAX_LOOP_LIMIT_HIT" in str(exc.value)


@pytest.mark.skipif(
    not os.path.isfile(
        os.path.join(
            os.path.dirname(__file__),
            "../../src/python/code/gnoll/c_build/dice.so",
        )
    ),
    reason="Native dice.so not built",
)
def test_normal_roll_still_works():
    from gnoll import roll

    code, result, _ = roll("2d6", breakdown=False)
    assert code == 0
    assert isinstance(result, list)
