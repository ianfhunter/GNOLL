import subprocess
import os
import sys
import platform
import cppyy
import io
from contextlib import redirect_stdout, redirect_stderr
from importlib import reload

# BUILD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../build'))
BUILD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../c_build'))
C_HEADER = os.path.join(os.path.dirname(__file__), '../c_includes')
C_SHARED_LIB = os.path.join(BUILD_DIR, 'dice.so')
cppyy.c_include(C_HEADER)
cppyy.load_library(C_SHARED_LIB)

import tempfile

def roll(s, verbose=False, mock=None, quiet=True, mock_const=3):
    if verbose: print("Rolling: ", s)


    temp = tempfile.NamedTemporaryFile(prefix="dicetower_roll_", suffix=".die")
    f = str(temp.name)
    print("File: ", f)

    if mock is None:
        return_code = cppyy.gbl.roll_and_write(s, f)
    else:
        # Testing Only
        return_code = cppyy.gbl.mock_roll(s, f, mock, quiet, mock_const)

    with open(temp.name) as f:
        results = f.readlines()
        if verbose:
            print("--Parsed Output--")
            print(results)
            print("--Parsed Output END--")
        out = results[0]

        for i in results:
            if "error" in i:
                return_code = 1

    try:
        out = int(out)
    except:
        pass

    return int(return_code), out


if __name__=="__main__":
    arg = "".join(sys.argv[1:])
    arg = arg if arg != "" else "1d20"
    code, r = roll(arg, verbose=True)
    print("Result:", r, ", Exit Code:", code)
