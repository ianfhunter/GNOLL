import os
import sys
import tempfile
import cppyy

BUILD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "c_build"))
if not os.path.exists(BUILD_DIR):
    BUILD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../build"))

C_HEADER = os.path.join(os.path.dirname(__file__), "c_includes")
if not os.path.exists(C_HEADER):
    C_HEADER = os.path.join(os.path.dirname(__file__), "../../../grammar")

C_SHARED_LIB = os.path.join(BUILD_DIR, "dice.so")


cppyy.c_include(os.path.join(C_HEADER, "shared_header.h"))
cppyy.load_library(C_SHARED_LIB)


def roll(s, verbose=False, mock=None, quiet=True, mock_const=3):
    if verbose:
        print("Rolling: ", s)

    temp = tempfile.NamedTemporaryFile(prefix="dicetower_roll_", suffix=".die")
    f = str(temp.name)
    if verbose:
        print("File: ", f)

    cppyy.gbl.reset()

    if mock is None:
        return_code = cppyy.gbl.roll_and_write(s, f)
    else:
        # Testing Only
        return_code = cppyy.gbl.mock_roll(s, f, mock, quiet, mock_const)

    if verbose:
        print("Temp File:", temp.name)
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
    except ValueError:
        pass

    return int(return_code), out


if __name__ == "__main__":
    arg = "".join(sys.argv[1:])
    arg = arg if arg != "" else "1d20"
    code, r = roll(arg, verbose=True)
    print("Result:", r, ", Exit Code:", code)
