import os
import matplotlib.pyplot as plt
import time
from rpg_dice import roll as rpgdice_roll
from dice import roll as dice_roll
from python_dice import PythonDiceInterpreter
from d20 import roll as d20_roll
import importlib.util as iu
import func_timeout

SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/python/code/gnoll/"))
m = os.path.join(SRC_DIR, "parser.py")
spec = iu.spec_from_file_location("dt", m)
dt = iu.module_from_spec(spec)
spec.loader.exec_module(dt)

gnoll_roll = dt.roll

def pythondice_roll(s):
    interpreter = PythonDiceInterpreter()
    return interpreter.roll([s])


# X axis = Roll
# Y axis = Time

shared_x = range(0, 10)
TIMEOUT = 300

configurations = {
    "GNOLL": {
        "roll_fn": gnoll_roll,
        "color": "b",
        "marker":"o"
    },
    "RPG Dice": {
        "roll_fn": rpgdice_roll,
        "color": "g",
        "marker": "^"
    },
    "Dice": {
        "roll_fn": dice_roll,
        "color": "r",
        "marker": "s"
    },
    "PythonDice":{
        "roll_fn": pythondice_roll,
        "color": "c",
        "marker": "x",
        "limit": 100000000 # Crashes Python after this
    },
    "d20":{
        "roll_fn": d20_roll,
        "color": "y",
        "marker": "1"
    }
}

# Data gather
for key in configurations:
    print("Profiling: ", key)
    c = configurations[key]
    y = []
    dx = []

    for x in shared_x:
        n = 10**x

        if "limit" in c and n >= c["limit"]:
            break

        r = f"{n}d{n}"
        print(f"\t{r}")
        roll_fn = c["roll_fn"]
        try:
            time1 = time.time()
            func_timeout.func_timeout(
                TIMEOUT, roll_fn, args=[r]
            )
            time2 = time.time()
            total_time = time2 - time1
            y.append(total_time*1000)
            dx.append(x)
        except (Exception, func_timeout.FunctionTimedOut) as e:
            print(f"Err: {key}:{r}")
            print("\t", e)
            break

    if len(dx):
        plt.plot(
            dx, y,
            color=c["color"],
            marker=c["marker"]
        )

# Configuration and Output
plt.xlabel("Dice Roll (10^N)d(10^N)")
plt.ylabel("Time (ms)")
plt.title('Python Library comparison')

plt.yscale('log')
plt.legend(configurations.keys())

this_folder = os.path.dirname(__file__)
output_file = os.path.join(this_folder, "../../doc/JOSS/py.PNG")
plt.savefig(output_file)
plt.show()
