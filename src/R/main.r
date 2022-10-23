print("Hello GNOLL")

library.dynam(
    "dice.so", 
    "GNOLL", 
    "",
    "../../build/",
    verbose = True
)

return_code <- GNOLL.roll_and_write(
    "1d20",
    "output.dice"
)

print(return_code)
