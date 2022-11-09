print("Hello GNOLL")

dyn.load("build/r/dice.so")

return_code <- .C("roll_and_write_2d_pointers",
    "1d20",
    "output.dice"
)
assert("GNOLL Exit code was SUCCESS", (return_code==0))

print(return_code)
