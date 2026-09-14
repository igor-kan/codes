local M = {}

local function new_dsu(n)
    local parent, rank = {}, {}
    for i = 1, n do parent[i] = i; rank[i] = 0 end
    return { parent = parent, rank = rank }
end

local function find(dsu, x)
    if dsu.parent[x] ~= x then
        dsu.parent[x] = find(dsu, dsu.parent[x])
    end
    return dsu.parent[x]
end

local function union(dsu, x, y)
    local rx, ry = find(dsu, x), find(dsu, y)
    if rx == ry then return end
    if dsu.rank[rx] < dsu.rank[ry] then
        dsu.parent[rx] = ry
    elseif dsu.rank[rx] > dsu.rank[ry] then
        dsu.parent[ry] = rx
    else
        dsu.parent[ry] = rx
        dsu.rank[rx] = dsu.rank[rx] + 1
    end
end

local function connected(dsu, x, y)
    return find(dsu, x) == find(dsu, y)
end

M.new = new_dsu
M.find = find
M.union = union
M.connected = connected

if not pcall(debug.getlocal, 4, 1) then
    local dsu = M.new(5)
    M.union(dsu, 1, 2)
    M.union(dsu, 2, 3)
    M.union(dsu, 4, 5)
    assert(M.connected(dsu, 1, 3), "union failed")
    assert(not M.connected(dsu, 1, 4), "spurious union")
    print("[Lua DSU] Disjoint set union verified")
end

return M
