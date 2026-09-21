include("singular_value_decomposition.jl")
using .SimpleSVD
using Test

@testset "SimpleSVD Tests" begin
    A = [3.0 0.0; 0.0 2.0]
    s1 = top_singular_value(A)
    @test isapprox(s1, 3.0, atol=1e-3)
end
