import os
import matplotlib.pyplot as plt
import time
import subprocess
from gnoll.parser import roll as gnoll_roll

troll_exec = os.path.join(
    os.path.expanduser('~'),
    "troll"
)

time1 = 0  # Allow start time to be overridden when prep needed

def troll_roll(s):
    global troll_exec
    global time1
    with fopen("test.t") as f:
        f.write(f"sum {s}")
    time1 = time.time()
    subprocess.run([troll_exec, "test.t"])

# X axis = Roll
# Y axis = Time

shared_x = [0,1,2,3,4,5,6]

configurations = {
    "GNOLL": {
        "roll_fn": gnoll_roll,
        "color": "b"
    },
    "TROLL": {
        "roll_fn": troll_roll,
        "color": "g"
    }
}


# Data gather
for key in configurations:
    print("Rolling: ", key)
    c = configurations[key]
    y = []
    dx = []

    for x in shared_x:
        n = 10**x
        r = f"{n}d{n}"
        time1 = time.time()
        try:
            result = c["roll_fn"](r)
            time2 = time.time()
            y.append((time2 - time1)*1000)
            dx.append(x)
        except Exception as e:
            print(f"Err: {key}:{r}")
            print("\t", e)

    if len(dx):
        plt.plot(
            dx, y,
            color=c["color"]
        )

# Configuration and Output
plt.xlabel("Dice Roll (10^N)d(10^N)")
plt.ylabel("Time (ms)")
plt.title('Cmdline Library comparison')

plt.yscale('log')
plt.legend(configurations.keys())

this_folder = os.path.dirname(__file__)
output_file = os.path.join(this_folder, "../../doc/JOSS/cpp.PNG")
plt.savefig(output_file)
