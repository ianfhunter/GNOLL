#!/usr/bin/env python3

import pytest
from util import roll, Mock

@pytest.mark.parametrize("FD",["df", "dF", "df.2", "dF.2"])
def test_traditional_fate(FD):
    # Assure Symbols are correct
    # TODO: Maybe it would be better to return "PLUS", "BLANK" "MINUS"?
    result = roll(FD, mock_mode=Mock.RETURN_CONSTANT, mock_const=0)
    assert result == "+"
    result = roll(FD, mock_mode=Mock.RETURN_CONSTANT, mock_const=1)
    assert result == 0
    result = roll(FD, mock_mode=Mock.RETURN_CONSTANT, mock_const=2)
    assert result == "-"

@pytest.mark.parametrize("FD",["df.2", "dF.2"])
def test_large_alt_fate_2(FD):
    result = roll(FD, mock_mode=Mock.RETURN_CONSTANT, mock_const=0)
    assert result == "+"
    result = roll(FD, mock_mode=Mock.RETURN_CONSTANT, mock_const=1)
    assert result == 0
    result = roll(FD, mock_mode=Mock.RETURN_CONSTANT, mock_const=2)
    assert result == 0
    result = roll(FD, mock_mode=Mock.RETURN_CONSTANT, mock_const=3)
    assert result == 0
    result = roll(FD, mock_mode=Mock.RETURN_CONSTANT, mock_const=4)
    assert result == 0
    result = roll(FD, mock_mode=Mock.RETURN_CONSTANT, mock_const=5)
    assert result == "-"

@pytest.mark.parametrize("FD",["df.3", "dF.9"])
def test_large_alt_fate_N(FD):
    result = roll(FD, mock_mode=Mock.RETURN_CONSTANT, mock_const=0)
    assert result == "+"
    result = roll(FD, mock_mode=Mock.RETURN_CONSTANT, mock_const=1)
    assert result == "-"

def test_multidie():
    result = roll("2dF", mock_mode=Mock.RETURN_CONSTANT, mock_const=2)
    assert result == ['-', '-']


def test_fate_addition():
    # Addition = Concatination
    result = roll("df+df", mock_mode=Mock.RETURN_CONSTANT, mock_const=2)
    assert result == ['-', '-']

def test_fate_numeral_interoperability():
    # Most of the time, using the two together doesn't make sense
    with pytest.raises(Exception):
        result = roll("d10+dF", mock_mode=(0,1))
    with pytest.raises(Exception):
        result = roll("d10-dF", mock_mode=(0,1))

    # Much arithmithic is ambigious with symbols
    # e.g.
    # dF * 2 could mean:
    # - roll 2 dF dice (2dF -> -+)
    # or
    # - multiply the result of dF by 2 (+ -> ++)
    # Unless there is evidence of that priority defined somewhere
    with pytest.raises(Exception):
        result = roll("d10-d10", mock_mode=(0,1))
    with pytest.raises(Exception):
        result = roll("dF*2")
    with pytest.raises(Exception):
        result = roll("dF*dF")
    with pytest.raises(Exception):
        result = roll("dF/2")
    with pytest.raises(Exception):
        result = roll("dF/dF")
    with pytest.raises(Exception):
        # We could perhaps use modulo as a counter
        # or some other function.
        # But for now, its undefined behaviour
        result = roll("dF%2")
    with pytest.raises(Exception):
        result = roll("dF%dF")
