using LinearAlgebra

function bit_reverse_permute!(a::Vector{ComplexF64})
    n = length(a)
    j = 0
    for i in 1:(n - 1)
        bit = n >> 1
        while j & bit != 0
            j ⊻= bit
            bit >>= 1
        end
        j ⊻= bit
        if i < j
            a[i + 1], a[j + 1] = a[j + 1], a[i + 1]
        end
    end
end

function fft_radix2!(a::Vector{ComplexF64}, invert::Bool=false)
    n = length(a)
    @assert ispow2(n) "Length must be power of 2"
    bit_reverse_permute!(a)

    len = 2
    while len <= n
        sign = invert ? 1.0 : -1.0
        angle = 2.0 * π / len * sign
        wlen = exp(im * angle)
        half = len >> 1
        
        i = 1
        while i <= n
            w = 1.0 + 0.0im
            for j in 0:(half - 1)
                u = a[i + j]
                v = a[i + j + half] * w
                a[i + j] = u + v
                a[i + j + half] = u - v
                w *= wlen
            end
            i += len
        end
        len <<= 1
    end

    if invert
        a ./= n
    end
    return a
end

# Verification
let
    data = ComplexF64[1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]
    original = copy(data)
    fft_radix2!(data, false)
    fft_radix2!(data, true)
    @assert maximum(abs.(data .- original)) < 1e-10
    println("[Julia FFT] Radix-2 in-place FFT validated.")
end
