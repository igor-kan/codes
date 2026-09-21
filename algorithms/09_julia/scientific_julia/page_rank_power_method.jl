module PageRank
export power_iteration_pagerank

function power_iteration_pagerank(M::Matrix{Float64}, d::Float64=0.85, iters::Int=50)
    n = size(M, 1)
    r = fill(1.0 / n, n)
    for _ in 1:iters
        r = d .* (M * r) .+ (1.0 - d) / n
    end
    return r
end
end
