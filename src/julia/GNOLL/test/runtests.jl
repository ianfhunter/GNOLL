using Pkg

lib_location = joinpath(@__DIR__, "..")
Pkg.develop(PackageSpec(path=lib_location))

using GnollDiceNotation
using Test

@testset "GnollDiceNotation.jl" begin
    # Write your tests here.
    rolled = GnollDiceNotation.roll("1d20")
    rolled = parse(Int64, rolled)
    @test rolled >= 1
    @test rolled <= 20
end
