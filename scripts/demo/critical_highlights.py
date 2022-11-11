import importlib.util as iu
import os
import re
import sys
from collections import Counter

# Copy-Pasted from test/util.py. Real app would just import gnoll from pypi
SRC_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../src/python/code/gnoll/")
)
m = os.path.join(SRC_DIR, "parser.py")
spec = iu.spec_from_file_location("dt", m)
dt = iu.module_from_spec(spec)
spec.loader.exec_module(dt)

roll = dt.roll

GREEN = '\033[92m'
RED = '\033[91m'
ENDC = '\033[0m'

def format_roll(s):
    _, dice, breakdown = roll(s)
    s_new = s
    for x in range(2):
        s_new = re.sub(r'[0-9]*d[0-9]+', str(breakdown[x][0]), s_new, count=1)
    s_new = re.sub(r'(^|\+)1($|\+)', fr"\1{RED}1{ENDC}\2", s_new)
    s_new = re.sub(r'(^|\+)20($|\+)', fr"\1{GREEN}20{ENDC}\2", s_new)
    print(f"Roll Request: '{s}'")
    print("Result:", s_new)
    

def main():
    """Format a Dice Roll"""
    # Roll 1.
    for x in range(100):
        format_roll("d20+d20")


if __name__ == "__main__":
    main()