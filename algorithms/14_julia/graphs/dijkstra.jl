# Dijkstra's Algorithm in Julia (CLRS 3rd Ed. Chapter 24.3)

function dijkstra(n::Int, adj::Vector{Vector{Tuple{Int, Float64}}}, source::Int)
    dist = fill(Inf, n)
    visited = fill(false, n)
    dist[source] = 0.0

    for _ in 1:n
        u = -1
        for i in 1:n
            if !visited[i] && (u == -1 || dist[i] < dist[u])
                u = i
            end
        end
        if dist[u] == Inf
            break
        end
        visited[u] = true

        for (v, w) in adj[u]
            if dist[u] + w < dist[v]
                dist[v] = dist[u] + w
            end
        end
    end
    return dist
end

adj = [
    [(2, 4.0), (3, 1.0)],
    [(4, 1.0)],
    [(2, 2.0), (4, 5.0)],
    Tuple{Int, Float64}[]
]
d = dijkstra(4, adj, 1)
@assert d[4] == 4.0
println("Julia Dijkstra verified.")
