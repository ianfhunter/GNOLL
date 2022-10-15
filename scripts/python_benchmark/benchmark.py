import os
import matplotlib.pyplot as plt
import numpy as np
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

shared_x = [1,10,100,1000,10000,100000,1000000]

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
    "PythonDice":{
        "roll_fn": pythondice_roll,
        "color": "c"
    }
}


# Data gather
for key in configurations:
    c = configurations[key]
    y = []

    for x in shared_x:
        result = c["roll_fn"](f"{x}d{x}")
        y.append(result)
  
    plt.plot(
        shared_x, y, 
        color=c["color"]
       # legend=key
    )
    
# Configuration and Output
plt.xlabel("Dice Roll (10^N)d(10^N)")
plt.ylabel("Time (s)")
plt.title('Python Library comparison')

plt.set_yscale('log')
plt.legend(configurations.keys())

this_folder = os.path.dirname(__file__)
output_file = os.path.join(this_folder, "../../doc/JOSS/py.PNG")
plt.savefig(output_file)
