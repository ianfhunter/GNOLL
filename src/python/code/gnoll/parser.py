import os
import sys
import tempfile
from ctypes import cdll

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


def roll(s, verbose=False, mock=None, mock_const=3, breakdown=False):
    temp = tempfile.NamedTemporaryFile(prefix="gnoll_roll_",
                                       suffix=".die",
                                       delete=False)

    def make_native_type(v):
        if v == "0":
            return 0
        if v == "":
            return "NULL"
        try:
            return int(v)
        except ValueError:
            return v

    def extract_from_dice_file(lines, seperator):
        v = [x.split(seperator)[:-1] for x in lines if seperator in x]
        v = [list(map(make_native_type, x)) for x in v]
        return v

    die_file = temp.name
    os.remove(die_file)

    out_file = str(die_file).encode("ascii")
    if verbose:
        print("Rolling: ", s)
        print("Output in:", out_file)

    with pipes() as (out, err):
        s = s.encode("ascii")

        return_code = libc.roll_full_options(
            s,
            out_file,
            False,  # enable_verbose
            breakdown,  # enable_introspect
            mock is not None,  # enable_mock
            mock,
            mock_const,
        )

    if verbose:
        print("---stdout---")
        print(out.read())
        print("---stderr---")
        print(err.read())

    if return_code != 0:
        raise_gnoll_error(return_code)

    with open(out_file, encoding="utf-8") as f:
        lines = f.readlines()

    dice_breakdown = extract_from_dice_file(lines, ",")
    result = extract_from_dice_file(lines, ";")

    return int(return_code), result, dice_breakdown


if __name__ == "__main__":
    arg = "".join(sys.argv[1:])
    arg = arg if arg != "" else "1d20"
    code, r, breakdown = roll(arg, verbose=False)
    print(f"""
[[GNOLL Results]]
Dice Roll:      {arg}
Result:         {r}
Exit Code:      {code}, 
Dice Breakdown: {breakdown}""")
