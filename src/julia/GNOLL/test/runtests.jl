using Pkg

lib_location = joinpath(@__DIR__, "..")
Pkg.develop(PackageSpec(path=lib_location))

using GNOLL
using Test

@testset "GNOLL.jl" begin
    # Write your tests here.
    rolled = GNOLL.roll("1d20")
    rolled = parse(Int64, rolled)
    @test rolled >= 1
    @test rolled <= 20
end
