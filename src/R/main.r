# print("Hello GNOLL")

dyn.load("build/r/dice.so")

fn = "output.dice"
if(file.exists(fn)){
    file.remove(fn)
}

return_code = as.integer(-1)
error_code = .C(
    "roll_and_write_R",
    value=return_code,
    "1d20",
    fn
)

if(error_code$value != 0){
    print(paste("GNOLL Error Code:", error_code$value))
    stop("GNOLL Exit code was not Success")
}

result <- readLines(fn, warn=FALSE)
tokens <- strsplit(result, ";")
int_tokens <- strtoi(tokens)

print(paste("GNOLL rolled:", result))

if(int_tokens[1] <= 0 | int_tokens[1] > 20){
    stop ("GNOLL rolled invalid value")
}


