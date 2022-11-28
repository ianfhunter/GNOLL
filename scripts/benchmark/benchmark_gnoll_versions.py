import importlib.util as iu
import os

from benchmark_core import BenchMarker

MK_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

print("======= Roll Wrappers ==========")
SRC_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../src/python/code/gnoll/")
)
m = os.path.join(SRC_DIR, "parser.py")
spec = iu.spec_from_file_location("dt", m)
dt = iu.module_from_spec(spec)
spec.loader.exec_module(dt)
gnoll_roll = dt.roll

stored_count = 0
stored = [
    15.959553718566895,
    4.039726257324219,
    4.144654273986816,
    2.02181339263916,
    2.6558542251586914,
    4.502716064453125,
    26.067476272583008,
    190.7038116455078,
    1894.7485908865929,
    23813.859303792316,
    None,
]


def stored_measurements():
    # Horrible, but gives at least a rough indication of performance comparisons
    # Cannot reload .so effectively in Python
    # Perhaps we can load from file that a previous cmdline generates
    # or - use cmdline interface instead

    global stored_count

    val = stored[stored_count]
    stored_count += 1
    return val


print("======= Benchmark Begins ==========")
bm = BenchMarker(end_range=11)

bm.add_function(
    "GNOLL Before", None, override=stored_measurements, color="r", marker="x"
)
bm.add_function("GNOLL After", gnoll_roll, color="b", marker="s")

bm.benchmark("Feature comparison")

this_folder = os.path.dirname(__file__)
output_file = os.path.join(this_folder, "../../doc/JOSS/feature_clt.PNG")
bm.save(output_file)
