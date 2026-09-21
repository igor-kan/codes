include("levenberg_marquardt.jl")
using .LevenbergMarquardt
using Test

@testset "LevenbergMarquardt Tests" begin
    @test lm_damping_step(1.0, true) == 0.1
    @test lm_damping_step(1.0, false) == 10.0
end
