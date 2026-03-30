"""Pre-check dice notation before calling the native parser (defense in depth)."""

import re

# Keep in sync with src/grammar/shared_header.h (GNOLL_MAX_*).
_MAX_DECIMAL_TOKEN_LEN = 64
_MAX_DICE_PER_ROLL = 1_000_000
_LLONG_MAX = 2**63 - 1

_DICE_PATTERN = re.compile(rb"(\d*)d(\d+)")


def validate_roll_string(s: str) -> None:
    """
    Reject pathological input: oversized decimal literals and per-roll dice counts
    beyond GNOLL_MAX_DICE_PER_ROLL. Raises GNOLLException to match native errors.
    """
    from . import GNOLLException

    roll_b = s.encode("ascii")
    i = 0
    n = len(roll_b)
    while i < n:
        if 48 <= roll_b[i] <= 57:
            start = i
            while i < n and 48 <= roll_b[i] <= 57:
                i += 1
            if i - start > _MAX_DECIMAL_TOKEN_LEN:
                raise GNOLLException("OUT_OF_RANGE")
            value = int(roll_b[start:i].decode("ascii"))
            if value > _LLONG_MAX:
                raise GNOLLException("OUT_OF_RANGE")
        else:
            i += 1

    for m in _DICE_PATTERN.finditer(roll_b):
        count_part, sides_part = m.group(1), m.group(2)
        dice_count = int(count_part) if count_part else 1
        die_sides = int(sides_part)
        if die_sides > _LLONG_MAX:
            raise GNOLLException("OUT_OF_RANGE")
        if dice_count > _MAX_DICE_PER_ROLL:
            raise GNOLLException("MAX_LOOP_LIMIT_HIT")
