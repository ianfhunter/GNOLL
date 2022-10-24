const gnoll = joinpath(@__DIR__, "../../build/dice.so")
exit_code = ccall((:roll_and_write, gnoll), Int, (Cstring, Cstring), "1d20", "jl.dice")
