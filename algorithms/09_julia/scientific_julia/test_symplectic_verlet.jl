include("symplectic_verlet.jl")
using .SymplecticVerlet
using Test

@testset "SymplecticVerlet Tests" begin
    # Harmonic oscillator V(q) = 1/2 q^2 -> grad V = q
    q, p = verlet_step(1.0, 0.0, q -> q, 0.01)
    @test q < 1.0
    @test p < 0.0
end
