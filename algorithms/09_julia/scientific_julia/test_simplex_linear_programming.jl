include("simplex_linear_programming.jl")
using .SimplexLP
using Test

@testset "SimplexLP Tests" begin
    @test canonical_slack_count(5) == 5
end
