const gnoll = joinpath(@__DIR__, "../../build/dice.so")
gnoll_file = "jl.dice"
exit_code = ccall((:roll_and_write, gnoll), Int, (Cstring, Cstring), "1d20", gnoll_file)
@printf("Exit Code: %i", exit_code) 
f = open(gnoll_file, "r")
while ! eof(f) 
     s = readline(f)         
     println("$s")
end
close(f)
