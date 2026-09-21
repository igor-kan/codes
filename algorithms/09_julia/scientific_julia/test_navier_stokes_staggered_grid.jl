include("navier_stokes_staggered_grid.jl")
using .StaggeredGrid
using Test

@testset "StaggeredGrid Tests" begin
    u = [1.0 1.0; 2.0 2.0]
    v = [0.0 0.0; 0.0 0.0]
    rhs = pressure_poisson_rhs(u, v, 1.0, 0.1)
    @test rhs[1, 1] == 10.0
end
