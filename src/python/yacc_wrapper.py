import subprocess
import os

BUILD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../build'))

def roll(s):
    print("Rolling: ", s)
    # Todo: Threadsafe
    fn = os.path.join(BUILD_DIR, "parse.request")
    with open(fn, "w") as f:
        f.write(s)


    cmd = os.path.join(BUILD_DIR, "dice")
    parser = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    out, err = parser.communicate(s.encode("ascii"))
    return_code = parser.returncode

    out = out.decode("ascii").replace("\n","")

    print(out)
    print(return_code)
    return int(return_code), int(out)


if __name__=="__main__":
    roll("1d3")