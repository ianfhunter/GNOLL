#!/usr/bin/env python3

import os
from glob import glob

import pytest
from util import Mock, error_handled_by_gnoll, roll


@pytest.mark.parametrize(
    "r,out,mock",
    [
        ("#MY_DIE=d{A};d4", 3, Mock.RETURN_CONSTANT),
        ("#MY_EYE=d{A};2d4", 6, Mock.RETURN_CONSTANT),
    ],
)
def test_macro_storage(r, out, mock):
    result, _ = roll(r, mock_mode=mock)
    assert result == out


@pytest.mark.parametrize("r,out,mock", [("#MY_DIE=d{A};@MY_DIE", "A", Mock.NO_MOCK)])
def test_macro_usage(r, out, mock):
    result, _ = roll(r, mock_mode=mock)
    assert result == out


@pytest.mark.skip("Currently no support for rerolling operations like Addition")
def test_d66():
    r = "#DSIXTYSIX=(d6*10)+d6;@DSIXTYSIX"
    result, _ = roll(r, mock_mode=Mock.RETURN_CONSTANT, mock_const=3)
    assert result == 33


# @pytest.mark.skip("TEMP")
def test_multiple_internal_calls_macros():
    r = "#TEST=d{A,B,C,D,E,F,G,H};@TEST;@TEST;@TEST;@TEST;@TEST;@TEST;@TEST;"
    result, _ = roll(r)
    assert not all(r == result[0] for r in result)

# @pytest.mark.skip("TEMP")
def test_multiple_external_calls_macros():
    result = []
    r = "#TEST=d{A,B,C,D};@TEST;"
    for _ in range(20):
        x= roll(r)
        result.append(x)
        print(x)
    assert not all(r == result[0] for r in result)


def test_undefined_macro():
    try:
        roll("@SOME_MACRO")
    except Exception as e:
        error_handled_by_gnoll(e)


def test_predefined_macro():
    r = roll("@ORACLE", builtins=True)[0]
    assert r in ["YES", "YES_AND", "YES_BUT", "NO", "NO_AND", "NO_BUT"]


def test_builtins():
    # Check that builtins are valid calls
    here = os.path.dirname(os.path.abspath(__file__))
    d = os.path.join(here, "../../builtins/*.dice")
    for name in glob(d):
        with open(name, encoding="utf_8") as f:
            for macro in f.readlines():
                macro = macro.strip("\n")
                if macro == "":
                    continue
                print("MACRO:", macro)
                roll(f"{macro};d20")
