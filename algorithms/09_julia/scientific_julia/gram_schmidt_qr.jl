module GramSchmidtQR
export modified_gram_schmidt

function modified_gram_schmidt(A::Matrix{Float64})
    m, n = size(A)
    Q = copy(A)
    R = zeros(Float64, n, n)
    for j in 1:n
        for i in 1:j-1
            R[i, j] = sum(Q[:, i] .* Q[:, j])
            Q[:, j] .-= R[i, j] .* Q[:, i]
        end
        R[j, j] = sqrt(sum(Q[:, j].^2))
        Q[:, j] ./= R[j, j]
    end
    return Q, R
end
end
