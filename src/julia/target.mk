.PHONY: julia
julia: clean yacc lex compile shared
	julia src/julia/main.jl
