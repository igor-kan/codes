include("random_walk_hitting_time.jl")
using .RandomWalkHitting
using Test

@testset "RandomWalkHitting Tests" begin
    @test expected_hitting_time_1d(3, 4) == 12
end
