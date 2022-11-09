print("Hello GNOLL")

dyn.load("build/r/dice.so")

return_code <- .C("roll_and_write_2d_pointers",
    "1d20",
    "output.dice"
)

print(return_code)
