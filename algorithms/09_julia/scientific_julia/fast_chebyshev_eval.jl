module FastChebyshev
export clenshaw_chebyshev

function clenshaw_chebyshev(coeffs::Vector{Float64}, x::Float64)
    n = length(coeffs)
    b2 = 0.0
    b1 = 0.0
    for k in n:-1:2
        b0 = coeffs[k] + 2.0 * x * b1 - b2
        b2 = b1
        b1 = b0
    end
    return coeffs[1] + x * b1 - b2
end
end
