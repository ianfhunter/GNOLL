
f = "output.dice"
delete(f)

// roll_and_write("d20", f)

data =textread(f,"%s")
print("Result: %s\n", data)