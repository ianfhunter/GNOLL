import matplotlib.pyplot as plt
import importlib.util as iu
import os
from scipy import stats

# Copy-Pasted from test/util.py
SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/python/code/gnoll/"))
m = os.path.join(SRC_DIR, "parser.py")
spec = iu.spec_from_file_location("dt", m)
dt = iu.module_from_spec(spec)
spec.loader.exec_module(dt)

roll = dt.roll

import time

def main():

    results = []
    die = "10d200"
    minutes = 5
    t_end = time.time() + 60 * minutes

    # while time.time() < t_end:
    for _ in range(10000):
        r = roll(die)
        results.append(r[1])

    k2, p = stats.normaltest(results)
    print("P-Value:", p)

    plt.hist(results, bins=1000)
    plt.title("GNOLL Histogram")
    plt.show()

if __name__ == "__main__":
    main()
