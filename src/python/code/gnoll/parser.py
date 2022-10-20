import os
import sys
import tempfile

import cppyy

BUILD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "c_build"))
C_HEADER = os.path.join(os.path.dirname(__file__), "c_includes")
C_SHARED_LIB = os.path.join(BUILD_DIR, "dice.so")

cppyy.c_include(os.path.join(C_HEADER, "shared_header.h"))
cppyy.c_include(os.path.join(C_HEADER, "dice_logic.h"))
cppyy.load_library(C_SHARED_LIB)


class GNOLLException(Exception):
    def __init__(self, v):
        Exception.__init__(self, v)


def raise_gnoll_error(value):
    d = [
        None,
        GNOLLException("BAD_ALLOC"),
        GNOLLException("BAD_FILE"),
        GNOLLException("NOT_IMPLEMENTED"),
        GNOLLException("INTERNAL_ASSERT"),
        GNOLLException("UNDEFINED_BEHAVIOUR"),
        GNOLLException("BAD_STRING"),
        GNOLLException("OUT_OF_RANGE"),
        GNOLLException("IO_ERROR"),
        GNOLLException("MAX_LOOP_LIMIT_HIT"),
        GNOLLException("SYNTAX_ERROR"),
        GNOLLException("DIVIDE_BY_ZERO"),
    ]
    err = d[value]
    if err is not None:
        raise err


def roll(s, verbose=False, mock=None, quiet=True, mock_const=3):
    temp = tempfile.NamedTemporaryFile(prefix="gnoll_roll_",
                                       suffix=".die",
                                       delete=False)
    die_file = temp.name
    os.remove(die_file)

    f = str(die_file)
    if verbose:
        print("Rolling: ", s)

    cppyy.gbl.reset_mocking()
    if mock is None:
        return_code = cppyy.gbl.roll_and_write(s, f)
    else:
        return_code = cppyy.gbl.mock_roll(s, f, mock, quiet, mock_const)

    if return_code != 0:
        raise_gnoll_error(return_code)

    with open(temp.name) as f:
        results = f.readlines()[0].split(";")[:-1]

        if isinstance(results, list):
            if len(results) == 1:
                results = results[0]

        if isinstance(results, list):
            if all(x.lstrip("-").isdigit() for x in results):
                results = [int(o) for o in results]

        elif results.lstrip("-").isdigit():
            results = int(results)

    return int(return_code), results


if __name__ == "__main__":
    arg = "".join(sys.argv[1:])
    arg = arg if arg != "" else "1d20"
    code, r = roll(arg, verbose=True)
    print(f"Result: {r}. Exit Code: {code}")
