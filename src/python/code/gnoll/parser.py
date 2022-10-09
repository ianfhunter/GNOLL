import os
import sys
import tempfile

import cppyy
from enum import Enum

BUILD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "c_build"))
C_HEADER = os.path.join(os.path.dirname(__file__), "c_includes")
C_SHARED_LIB = os.path.join(BUILD_DIR, "dice.so")

cppyy.c_include(os.path.join(C_HEADER, "shared_header.h"))
cppyy.c_include(os.path.join(C_HEADER, "dice_logic.h"))
cppyy.load_library(C_SHARED_LIB)


class GNOLLException(Exception):
    def __init__(self, v):
        Exception.__init__(self, 'Tax ID expired')

def RaiseGNOLLError(v):
    d = [
        None,
        GNOLLException("BAD_ALLOC"),
        GNOLLException("BAD_FILE"),
        GNOLLException("NOT_IMPLEMENTED"),
        GNOLLException("INTERNAL_ASSERT"),
        GNOLLException("UNDEFINED_BEHAVIOUR"),
        GNOLLException("BAD_STRING"),
        GNOLLException("OUT_OF_RANGE"),
        GNOLLException("IO_ERROR")
    ]
    raise d[v]

def roll(s, verbose=False, mock=None, quiet=True, mock_const=3):     
    if verbose:
        print("Rolling: ", s)

    temp = tempfile.NamedTemporaryFile(prefix="gnoll_roll_", suffix=".die")
    temp.name = "dice.roll"
    try:
        os.remove(temp.name)
    except FileNotFoundError:
        pass
    f = str(temp.name)
    if verbose:
        print("File: ", f)

    cppyy.gbl.reset_mocking()
    if mock is None:
        return_code = cppyy.gbl.roll_and_write(s, f)
    else:
        # Testing Only
        return_code = cppyy.gbl.mock_roll(s, f, mock, quiet, mock_const)
    
    if(return_code != 0):
        RaiseGNOLLError(return_code)

    if verbose:
        print("Temp File:", temp.name)
    with open(temp.name) as f:
        results = f.readlines()[0].split(";")[:-1]
        if verbose:
            print("--Parsed Output--")
            print(results)
            print("--Parsed Output END--")
        out = results

        for i in results:
            if "error" in i:
                return_code = 1

    if isinstance(out, list) and len(out) == 1:
        out = out[0]

    if isinstance(out, list):
        if all([x.lstrip("-").isdigit() for x in out]):
            out = [int(o) for o in out]
    elif out.lstrip("-").isdigit():
        out = int(out)

    return int(return_code), out


if __name__ == "__main__":
    arg = "".join(sys.argv[1:])
    arg = arg if arg != "" else "1d20"
    code, r = roll(arg, verbose=True)
    print(f"Result: {r}. Exit Code: {code}")
