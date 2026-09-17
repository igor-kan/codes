# Floyd-Warshall All-Pairs Shortest Paths in Julia (CLRS 3rd Ed. Chapter 25.2)

function floyd_warshall(matrix::Matrix{Float64})
    n = size(matrix, 1)
    dist = copy(matrix)

    for k in 1:n
        for i in 1:n
            for j in 1:n
                if dist[i, k] + dist[k, j] < dist[i, j]
                    dist[i, j] = dist[i, k] + dist[k, j]
                end
            end
        end
    end
    return dist
end

M = [0.0 3.0 Inf; 2.0 0.0 Inf; Inf 7.0 0.0]
D = floyd_warshall(M)
@assert D[2, 1] == 2.0
println("Julia Floyd-Warshall verified.")
