module DataStructures

mutable struct DSU
    parent::Vector{Int}
    rank::Vector{Int}
end

function DSU(n::Int)
    DSU(collect(1:n), zeros(Int, n))
end

function find!(dsu::DSU, x::Int)::Int
    if dsu.parent[x] != x
        dsu.parent[x] = find!(dsu, dsu.parent[x])
    end
    return dsu.parent[x]
end

function union!(dsu::DSU, x::Int, y::Int)
    rx = find!(dsu, x)
    ry = find!(dsu, y)
    rx == ry && return nothing
    if dsu.rank[rx] < dsu.rank[ry]
        dsu.parent[rx] = ry
    elseif dsu.rank[rx] > dsu.rank[ry]
        dsu.parent[ry] = rx
    else
        dsu.parent[ry] = rx
        dsu.rank[rx] += 1
    end
    return nothing
end

connected(dsu::DSU, x::Int, y::Int) = find!(dsu, x) == find!(dsu, y)

end

dsu = DataStructures.DSU(5)
DataStructures.union!(dsu, 1, 2)
DataStructures.union!(dsu, 2, 3)
DataStructures.union!(dsu, 4, 5)
@assert DataStructures.connected(dsu, 1, 3)
@assert !DataStructures.connected(dsu, 1, 4)
println("[Julia DSU] Disjoint set union verified")
