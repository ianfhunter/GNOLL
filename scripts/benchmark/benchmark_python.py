import os
from benchmark_core import BenchMarker

print("======= Benchmark Imports ==========")
from rpg_dice import roll as rpgdice_roll
from dice import roll as dice_roll
from python_dice import PythonDiceInterpreter
from d20 import roll as d20_roll
import importlib.util as iu

print("======= Roll Wrappers ==========")
SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/python/code/gnoll/"))
m = os.path.join(SRC_DIR, "parser.py")
spec = iu.spec_from_file_location("dt", m)
dt = iu.module_from_spec(spec)
spec.loader.exec_module(dt)

gnoll_roll = dt.roll

def pythondice_roll(s):
    interpreter = PythonDiceInterpreter()
    return interpreter.roll([s])

print("======= Benchmark Begins ==========")
bm = BenchMarker()

#bm.addFunction("GNOLL", gnoll_roll, color="b", marker="o")
bm.addFunction("RPG Dice", rpgdice_roll, color="g", marker="^")
#bm.addFunction("Dice", dice_roll, color="r", marker="x")
#bm.addFunction("PythonDice", pythondice_roll, color="c", marker="s", hard_limit=100000000)
#bm.addFunction("d20", d20_roll, color="y", marker="1")

bm.benchmark("Python Library comparison")

this_folder = os.path.dirname(__file__)
output_file = os.path.join(this_folder, "../../doc/JOSS/py.PNG")
bm.save(output_file)
