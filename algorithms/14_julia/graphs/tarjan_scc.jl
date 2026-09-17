# Tarjan's Strongly Connected Components in Julia

function tarjan_scc(n::Int, adj::Vector{Vector{Int}})
    index = fill(-1, n)
    lowlink = fill(-1, n)
    on_stack = fill(false, n)
    stack = Int[]
    sccs = Vector{Vector{Int}}()
    timer = 0

    function strongconnect(v::Int)
        index[v] = timer
        lowlink[v] = timer
        timer += 1
        push!(stack, v)
        on_stack[v] = true

        for w in adj[v]
            if index[w] == -1
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elseif on_stack[w]
                lowlink[v] = min(lowlink[v], index[w])
            end
        end

        if lowlink[v] == index[v]
            scc = Int[]
            while true
                w = pop!(stack)
                on_stack[w] = false
                push!(scc, w)
                if w == v
                    break
                end
            end
            push!(sccs, scc)
        end
    end

    for i in 1:n
        if index[i] == -1
            strongconnect(i)
        end
    end
    return sccs
end

adj = [[2], [3], [1, 4], [5], [6], [4]]
sccs = tarjan_scc(6, adj)
@assert length(sccs) == 2
println("Julia Tarjan SCC verified.")
