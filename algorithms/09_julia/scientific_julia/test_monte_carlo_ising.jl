include("monte_carlo_ising.jl")
using .MonteCarloIsing
using Test

@testset "MonteCarloIsing Tests" begin
    spins = ones(Int, 2, 2)
    e = ising_energy_2d(spins, 1.0)
    # 4 sites, each has 2 interactions: 4 * 2 = 8, E = -8
    @test e == -8.0
end
