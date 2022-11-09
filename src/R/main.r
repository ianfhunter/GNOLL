print("Hello GNOLL")

dyn.load("build/r/dice.so")

# TODO: delete file
return_code <- .C("roll_and_write_2d_pointers",
    "1d20",
    "output.dice"
)
assert("GNOLL Exit code was SUCCESS", (return_code==0))

print(return_code)

result <- read_lines("output.dice, skip = 0, n_max = -1)
result <- strtol(result)

assert("GNOLL rolled valid value", (result > 0), (result <= 20))


