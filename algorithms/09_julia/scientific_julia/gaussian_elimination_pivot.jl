module GaussianPivot
export solve_2x2

function solve_2x2(A::Matrix{Float64}, b::Vector{Float64})
    det = A[1,1]*A[2,2] - A[1,2]*A[2,1]
    x1 = (b[1]*A[2,2] - b[2]*A[1,2]) / det
    x2 = (A[1,1]*b[2] - A[2,1]*b[1]) / det
    return [x1, x2]
end
end
