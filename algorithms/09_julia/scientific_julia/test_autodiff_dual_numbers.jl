include("autodiff_dual_numbers.jl")
using .AutoDiffDual
using Test

@testset "AutoDiffDual Tests" begin
    f(x) = x * x # f'(x) = 2x
    d = dual_deriv(f, 3.0)
    @test d == 6.0
end
