import importlib.util as iu
import os

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Copy-Pasted from test/util.py
SRC_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../src/python/code/gnoll/"))
m = os.path.join(SRC_DIR, "__init__.py")
spec = iu.spec_from_file_location("dt", m)
dt = iu.module_from_spec(spec)
spec.loader.exec_module(dt)

roll = dt.roll


def main():
    num = 100000
    sides = 20

    results = []
    die = f"{num}d{sides}"

    for _ in range(10000):
        r = roll(die)
        results.append(r[1][0][0])

    _, p = stats.normaltest(results)
    print("P-Value:", p)

    print(results)
    print("Min:", np.min(results))
    print("Max:", np.max(results))

    num_bins = min(num * sides, 200)
    plt.hist(results, bins=num_bins)

    # Empirical average and variance are computed
    avg = np.mean(results)
    var = np.var(results)
    # From that, we know the shape of the fitted Gaussian.
    pdf_x = np.linspace(np.min(results), np.max(results), 100)
    pdf_y = 1.0 / np.sqrt(2 * np.pi * var) * np.exp(-0.5 *
                                                    (pdf_x - avg)**2 / var)

    plt.plot(pdf_x, pdf_y, "k--")

    plt.title(f"GNOLL Histogram: {die}")
    plt.show()


if __name__ == "__main__":
    main()
