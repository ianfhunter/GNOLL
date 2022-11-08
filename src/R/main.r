print("Hello GNOLL")

dyn.load("../../build/r/dice.so")

return_code <- GNOLL.roll_and_write(
    "1d20",
    "output.dice"
)

print(return_code)
