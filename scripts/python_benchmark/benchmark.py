import os
import matplotlib.pyplot as plt
import numpy as np
import time
from gnoll.parser import roll as gnoll_roll
from rpg_dice import roll as rpgdice_roll
from dice import roll as dice_roll
from python_dice import PythonDiceInterpreter

def pythondice_roll(s):
    interpreter = PythonDiceInterpreter()
    program = [s]
    return interpreter.roll(s)

# X axis = Roll
# Y axis = Time

shared_x = [0,1,2,3,4,5,6]

configurations = {
    "GNOLL": {
        "roll_fn": gnoll_roll,
        "color": "b"
    },
    "RPG Dice": {
        "roll_fn": rpgdice_roll,
        "color": "g"
    },
    "Dice": {
        "roll_fn": dice_roll,
        "color": "r"
    },
    #"PythonDice":{
    #    "roll_fn": pythondice_roll,
    #    "color": "c"
    #}
}


# Data gather
for key in configurations:
    print("Rolling: ", key)
    c = configurations[key]
    y = []

    for x in shared_x:
        n = 10**x
        time1 = time.time()
        result = c["roll_fn"](f"{n}d{n}")
        time2 = time.time()
        y.append((time2 - time1)*1000)
  
    plt.plot(
        shared_x, y, 
        color=c["color"]
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
