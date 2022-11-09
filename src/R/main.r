print("Hello GNOLL")

dyn.load("build/r/dice.so")

# TODO: delete file
return_code <- .C("roll_and_write_2d_pointers",
    "1d20",
    "output.dice"
)
if(return_code != 0){
    print(paste("GNOLL Error Code:", return_code))
    #stop("GNOLL Exit code was not Success")
)

result <- read_lines("output.dice", skip = 0, n_max = -1)
result <- strtol(result)

if(result <= 0 | result > 20)
    print(paste("GNOLL rolled:", result))
    stop ("GNOLL rolled invalid value")
)


