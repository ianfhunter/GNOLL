from distutils.log import error
import time
import func_timeout
import matplotlib
import matplotlib.pyplot as plt

class BenchMarker():

    TIMEOUT_MINUTES=5
    TIMEOUT_SECONDS = TIMEOUT_MINUTES*60
    AVERAGING_RUNS=50

    def __init__(self, start_range=0, end_range=10):
        self.competitors = []
        self.range = range(start_range, end_range)
        self.plt = plt

    def addFunction(self, name, f, color="r", marker="o", hard_limit=None):
        self.competitors.append({
            "name": name,
            "fn": f,
            "color": color,
            "marker": marker,
            "hard_limit": hard_limit
        })

    def benchmark(self, title):
        self.title = title
        for c in self.competitors:
            print(f"Benchmark::{c['name']}")

            shared_x = self.range     # X axis = Roll
            y = []                    # Y axis = Time

            for x in shared_x:
                n = 10**x

                lim = c["hard_limit"]
                if lim is not None and n >= lim:
                    # Stop. Fatal after this point.
                    break

                # Roll Construction
                r = f"{n}d{n}"
                print(f"\t{r}")
                roll_fn = c["fn"]

                # Write to file (TROLL hack)
                with open("test.t", "w") as f:
                    f.write(f"sum {r}")

                total_time = []
                count = 0
                errored = False

                for _ in range(self.AVERAGING_RUNS):
                    if errored:
                        break

                    # ------ BENCHMARK ------
                    time1 = time.time()
                    try:
                        func_timeout.func_timeout(
                            self.TIMEOUT_SECONDS, roll_fn, args=[r]
                        )
                    except (Exception, func_timeout.FunctionTimedOut) as e:
                        print(f"Err: {c['name']}:{r}")
                        print("\t", e)
                        errored = True
                    time2 = time.time()
                    # ------ END BENCHMARK ------
                    if not errored:
                        total_time.append(time2 - time1)                    
                        count += 1
                        if sum(total_time) > self.TIMEOUT_SECONDS:
                            # Looping has taken too long. Cut short.
                            break

                if count:
                    total_time = sum(total_time)/count
                    y.append(total_time*1000)

            if len(y):
                plt.plot(
                    shared_x[0:len(y)], y,
                    color=c["color"],
                    marker=c["marker"]
                )

        # Configuration and Output
        plt.xlabel("Dice Roll (10^N)d(10^N)")
        plt.ylabel("Time (ms)")
        plt.title(self.title)

        plt.yscale('log')
        # plt.ticklabel_format(style="plain", axis="y")
        ax = plt.gca()

        ax.get_yaxis().set_major_formatter(
            matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
        ax.get_xaxis().set_major_formatter(
            matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

        legend_labels = [c['name'] for c in self.competitors]
        plt.legend(legend_labels)

    def save(self, filename):
        self.plt.savefig(filename)
        self.plt.show()
