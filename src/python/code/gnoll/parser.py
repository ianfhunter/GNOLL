import os
import sys
import tempfile
from ctypes import cdll
from importlib import reload

from wurlitzer import pipes

BUILD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "c_build"))
C_SHARED_LIB = os.path.join(BUILD_DIR, "dice.so")

libc = cdll.LoadLibrary(C_SHARED_LIB)


class GNOLLException(Exception):

    def __init__(self, v):
        Exception.__init__(self, v)


def raise_gnoll_error(value):
    """Translates a GNOLL return code into a python
    Exception, which is then raised
    @value return code of GNOLL
    """
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
        GNOLLException("UNDEFINED_MACRO"),
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

    out_file = str(die_file).encode("ascii")
    if verbose:
        print("Rolling: ", s)
        print("Output in:", out_file)

    with pipes() as (out, err):
        s = s.encode("ascii")
        if mock is None:
            return_code = libc.roll_and_write(s, out_file)
        else:
            return_code = libc.mock_roll(s, out_file, mock, mock_const)

    if verbose:
        print("---stdout---")
        print(out.read())
        print("---stderr---")
        print(err.read())

    if return_code != 0:
        raise_gnoll_error(return_code)

    with open(out_file) as f:
        lines = f.readlines()
        results = lines[0].split(";")[:-1]

        if isinstance(results, list) and len(results) == 1:
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
