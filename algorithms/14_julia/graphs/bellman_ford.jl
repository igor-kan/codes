# Bellman-Ford Algorithm in Julia (CLRS 3rd Ed. Chapter 24.1)

struct Edge
    u::Int
    v::Int
    weight::Float64
end

function bellman_ford(n::Int, edges::Vector{Edge}, source::Int)
    dist = fill(Inf, n)
    dist[source] = 0.0

    for _ in 1:(n - 1)
        for e in edges
            if dist[e.u] != Inf && dist[e.u] + e.weight < dist[e.v]
                dist[e.v] = dist[e.u] + e.weight
            end
        end
    end

    for e in edges
        if dist[e.u] != Inf && dist[e.u] + e.weight < dist[e.v]
            error("Negative weight cycle detected")
        end
    end
    return dist
end

edges = [Edge(1, 2, -1.0), Edge(1, 3, 4.0), Edge(2, 3, 3.0), Edge(2, 4, 2.0), Edge(4, 2, 1.0), Edge(4, 3, 5.0)]
d = bellman_ford(4, edges, 1)
@assert d[2] == -1.0
println("Julia Bellman-Ford verified.")
