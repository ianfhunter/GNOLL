module GnollDiceNotation

using Printf

export roll

const gnoll = joinpath(@__DIR__, "../../../../build/dice.so")

function roll(s, verbose=false)
   
    gnoll_file = "jl.dice"
    rm(gnoll_file, force=true)
    exit_code = ccall((:roll_and_write, gnoll), Int, (Cstring, Cstring), "1d20", gnoll_file)
    
    if exit_code > 0
        throw(DomainError("GNOLL Error Code: ", exit_code))
    end
    f = open(gnoll_file, "r")
    while ! eof(f)
        s = readline(f) 
        s = strip(s, [';'])
        if verbose 
            println("$s")
        end
    end
    close(f)
    rm(gnoll_file, force=true)
    return s
end


end