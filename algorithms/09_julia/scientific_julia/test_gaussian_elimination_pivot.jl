include("gaussian_elimination_pivot.jl")
using .GaussianPivot
using Test

@testset "GaussianPivot Tests" begin
    A = [2.0 1.0; 1.0 3.0]
    b = [4.0, 7.0]
    x = solve_2x2(A, b)
    @test isapprox(x, [1.0, 2.0])
end
