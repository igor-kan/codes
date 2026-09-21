include("fast_chebyshev_eval.jl")
using .FastChebyshev
using Test

@testset "FastChebyshev Tests" begin
    # T_0(x) = 1, T_1(x) = x -> coeffs [1.0, 1.0] -> 1 + x
    val = clenshaw_chebyshev([1.0, 1.0], 0.5)
    @test isapprox(val, 1.5)
end
