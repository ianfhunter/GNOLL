module GnollDiceNotation

using Printf

export roll, validate_roll_request

const gnoll = joinpath(@__DIR__, "../../../../build/dice.so")

function validate_roll_request(s::AbstractString)
    code = ccall((:gnoll_validate_roll_request, gnoll), Cint, (Cstring,), s)
    return Int(code)
end

function roll(s, verbose=false)
    gnoll_file = "jl.dice"
    rm(gnoll_file, force=true)
    v = validate_roll_request(s)
    if v != 0
        throw(DomainError(v, "GNOLL validate error"))
    end
    exit_code = ccall((:roll_and_write, gnoll), Int, (Cstring, Cstring), s, gnoll_file)
    if exit_code != 0
        throw(DomainError(exit_code, "GNOLL roll error"))
    end
    f = open(gnoll_file, "r")
    last_line = ""
    while !eof(f)
        last_line = readline(f)
        if verbose
            println(last_line)
        end
    end
    close(f)
    rm(gnoll_file, force=true)
    return strip(last_line, [';'])
end

end
