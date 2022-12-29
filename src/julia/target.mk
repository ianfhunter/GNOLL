.PHONY: julia
julia: all
	julia src/julia/GNOLL/test/runtests.jl
