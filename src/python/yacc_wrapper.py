import subprocess
import os
import sys
import platform

BUILD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../build'))

def roll(s, verbose=False):
    if verbose: print("Rolling: ", s)
    # Todo: Threadsafe
    fn = os.path.join(BUILD_DIR, "parse.request").replace("\\","/")
    with open(fn, "w") as f:
        f.write(s)

    cmd = os.path.join(BUILD_DIR, "dice").replace("\\","/")
    parser = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    out, err = parser.communicate(s.encode("ascii"))
    return_code = parser.returncode

    out = out.decode("ascii").replace("\n","")
    print(out, err, return_code)
    if out.strip() == "":
        return_code = 1
        out = -123

    if verbose: print(out)
    if verbose: print(return_code)
    return int(return_code), int(out)


if __name__=="__main__":
    arg = sys.argv[1]
    arg = arg if arg != "" else "1d20"
    code, r = roll(arg, verbose=True)
    print("Result:", r)