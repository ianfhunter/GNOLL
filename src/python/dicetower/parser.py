import subprocess
import os
import sys
import platform
import cppyy
import io
from contextlib import redirect_stdout, redirect_stderr
from importlib import reload


BUILD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../build'))
C_HEADER = os.path.join(os.path.dirname(__file__), '../../grammar/shared_header.h')
C_SHARED_LIB = os.path.join(os.path.dirname(__file__), '../../../build/dice.so')
cppyy.c_include(C_HEADER)
cppyy.load_library(C_SHARED_LIB)

import tempfile

def roll(s, verbose=False):
    if verbose: print("Rolling: ", s)


    temp = tempfile.NamedTemporaryFile(prefix="dicetower_roll_", suffix=".die")
    f = str(temp.name)

    return_code = cppyy.gbl.roll_and_write(s, f)

    with open(temp.name) as f:
        results = f.readlines()
        if verbose or True:
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
