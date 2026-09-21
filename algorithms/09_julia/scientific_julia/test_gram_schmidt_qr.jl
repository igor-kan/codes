include("gram_schmidt_qr.jl")
using .GramSchmidtQR
using Test

@testset "GramSchmidtQR Tests" begin
    A = [1.0 1.0; 0.0 1.0]
    Q, R = modified_gram_schmidt(A)
    @test isapprox(sum(Q[:, 1] .* Q[:, 2]), 0.0, atol=1e-8)
end
