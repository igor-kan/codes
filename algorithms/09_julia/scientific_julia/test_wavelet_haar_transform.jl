include("wavelet_haar_transform.jl")
using .HaarWavelet
using Test

@testset "HaarWavelet Tests" begin
    sig = [1.0, 1.0, 2.0, 0.0]
    a, d = haar_step(sig)
    @test isapprox(a[1], sqrt(2.0))
    @test isapprox(d[1], 0.0)
end
