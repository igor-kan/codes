include("arnoldi_iteration.jl")
using .ArnoldiIteration
using Test

@testset "ArnoldiIteration Tests" begin
    @test arnoldi_basis_dim(5) == 6
end
