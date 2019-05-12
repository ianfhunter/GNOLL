
import numpy as np
import matplotlib.pyplot as plt

from dice import roll

from contextlib import contextmanager
import os
import sys


# Display Infrastructure
def graph(values, name):
    # Histogram of data
    values = np.array(values).flatten()

    plt.hist(values)

    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.title('Histogram of Dice Roll')
    plt.savefig(name+'.png')


def display(s):
    # Show a sample distribution
    v = []
    for n in range(10000):
        v.append(roll(s))

    if False:
        graph(v, s)
    return v


# Test Infrastructure

def spread(s, fail=False):

    v = []
    v.append(testLow(s))
    v.append(testHigh(s))
    vs = np.arange(v[0], v[1]+1)
    return vs


def not_random_lowest(randint_start=0, randint_end=99):
    return randint_start


def not_random_highest(randint_start=0, randint_end=99):
    return randint_end


def testHigh(s):
    return roll(s, override_rand=not_random_highest)


def testLow(s):
    return roll(s, override_rand=not_random_lowest)


def check_values(roll_text, lowest=0, highest=0, debug=False):

    data = spread(roll_text)

    expected = np.arange(lowest, highest+1)
    data = np.unique(np.array(data).flatten())
    if debug:
        print(data, expected)

    return np.array_equal(data, expected), data, expected, roll_text


@contextmanager
def suppress_prints():
    with open(os.devnull, "w") as devnull:
        old_stderr = sys.stderr
        old_stdout = sys.stdout
        sys.stderr = devnull
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stderr = old_stderr
            sys.stdout = old_stdout
