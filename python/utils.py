
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


    isInt = True
    try:
        v[0] = int(v[0])
        v[1] = int(v[1])
    except:
        isInt = False

    if isInt:
        vs = np.arange(v[0], v[1]+1)
        return vs
    else:
        return list(v)


def not_random_lowest(data):
    return data[0]


def not_random_highest(data):
    return data[-1]


def testHigh(s):
    return roll(s, override_rand=not_random_highest)


def testLow(s):
    return roll(s, override_rand=not_random_lowest)


def check_values(roll_text, lowest=0, highest=0, debug=False):

    data = spread(roll_text)

    isInt = True
    try:
        lowest = int(lowest)
        highest = int(highest)
    except:
        isInt = False

    if isInt:
        expected = np.arange(lowest, highest+1)
    else:
        lowest = str(lowest).strip().replace("\"", "")
        highest = str(highest).strip().replace("\"", "")

        if ":" in lowest:
            # Sequence
            lowest = [ x for x in lowest.split(":")]
            highest = [ x for x in highest.split(":")]

            try:
                lowestInt = [int(x) for x in lowest]
                highestInt = [int(x) for x in highest]
                lowest = lowestInt
                highest = highestInt
            except:
                pass

        expected = [lowest, highest]

    # debug = True
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
