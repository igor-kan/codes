include("spectral_fft_pde.jl")
using .SpectralFFTPDE
using Test

@testset "SpectralFFTPDE Tests" begin
    k = linear_dispersion_wavenumbers(8, 2.0 * pi)
    @test length(k) == 8
    @test k[1] == 0.0
end
