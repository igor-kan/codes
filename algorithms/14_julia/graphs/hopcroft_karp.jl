# Hopcroft-Karp Algorithm in Julia
# Maximum cardinality bipartite matching in O(E sqrt(V)).

function hopcroft_karp(nu::Int, nv::Int, adj::Vector{Vector{Int}})
    pair_u = zeros(Int, nu)
    pair_v = zeros(Int, nv)
    dist = fill(0, nu + 1)

    function bfs()
        queue = Int[]
        for u in 1:nu
            if pair_u[u] == 0
                dist[u] = 0
                push!(queue, u)
            else
                dist[u] = typemax(Int)
            end
        end
        dist[nu + 1] = typemax(Int)

        while !isempty(queue)
            u = popfirst!(queue)
            if dist[u] < dist[nu + 1]
                for v in adj[u]
                    pv = pair_v[v]
                    p_idx = pv == 0 ? nu + 1 : pv
                    if dist[p_idx] == typemax(Int)
                        dist[p_idx] = dist[u] + 1
                        if pv != 0
                            push!(queue, pv)
                        end
                    end
                end
            end
        end
        return dist[nu + 1] != typemax(Int)
    end

    function dfs(u::Int)
        if u != nu + 1
            for v in adj[u]
                pv = pair_v[v]
                p_idx = pv == 0 ? nu + 1 : pv
                if dist[p_idx] == dist[u] + 1 && dfs(p_idx)
                    pair_v[v] = u
                    pair_u[u] = v
                    return true
                end
            end
            dist[u] = typemax(Int)
            return false
        end
        return true
    end

    matching = 0
    while bfs()
        for u in 1:nu
            if pair_u[u] == 0 && dfs(u)
                matching += 1
            end
        end
    end
    return matching
end

adj = [[2, 3], [1], [2], [2, 4]]
m = hopcroft_karp(4, 4, adj)
@assert m == 4
println("Julia Hopcroft-Karp verified.")
