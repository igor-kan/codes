module SimpleSVD
export top_singular_value

function top_singular_value(A::Matrix{Float64}, iters::Int=50)
    v = ones(size(A, 2))
    v ./= sqrt(sum(v.^2))
    for _ in 1:iters
        v = A' * (A * v)
        v ./= sqrt(sum(v.^2))
    end
    return sqrt(sum((A * v).^2))
end
end
