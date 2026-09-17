# Cholesky LL^T in Julia (Numerical Recipes 3rd Ed. Chapter 2.6)

function cholesky_llt(A::Matrix{Float64})
    n = size(A, 1)
    L = zeros(Float64, n, n)

    for i in 1:n
        for j in 1:i
            s = 0.0
            for k in 1:(j - 1)
                s += L[i, k] * L[j, k]
            end
            if i == j
                val = A[i, i] - s
                @assert val > 0 "Matrix not positive definite"
                L[i, j] = sqrt(val)
            else
                L[i, j] = (A[i, j] - s) / L[j, j]
            end
        end
    end
    return L
end

A = [4.0 12.0 -16.0; 12.0 37.0 -43.0; -16.0 -43.0 98.0]
L = cholesky_llt(A)
@assert abs(L[1, 1] - 2.0) < 1e-6
println("Julia Cholesky LL^T verified.")
