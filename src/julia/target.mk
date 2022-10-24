.PHONY: julia
julia: clean yacc lex compile shared
	julia src/Julia/main.jl
