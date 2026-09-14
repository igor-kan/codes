module Graphs

using DataStructures

function bfs(adj::Dict{Int, Vector{Int}}, start::Int)
    visited = Set{Int}()
    q = Queue{Int}()
    order = Int[]

    push!(visited, start)
    enqueue!(q, start)

    while !isempty(q)
        node = dequeue!(q)
        push!(order, node)

        for neighbor in get(adj, node, Int[])
            if !(neighbor in visited)
                push!(visited, neighbor)
                enqueue!(q, neighbor)
            end
        end
    end
    return order
end

end
