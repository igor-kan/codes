include("page_rank_power_method.jl")
using .PageRank
using Test

@testset "PageRank Tests" begin
    # 2 symmetric nodes
    M = [0.0 1.0; 1.0 0.0]
    r = power_iteration_pagerank(M, 0.85, 20)
    @test isapprox(r[1], 0.5)
    @test isapprox(r[2], 0.5)
end
