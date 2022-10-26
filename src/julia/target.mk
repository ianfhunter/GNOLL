.PHONY: julia
julia: clean yacc lex compile shared
	julia src/julia/GNOLL/test/runtests.jl
