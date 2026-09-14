local M = {}

function M.z_algorithm(s)
    local n = #s
    local z = {}
    for i = 1, n do z[i] = 0 end
    if n > 0 then z[1] = n end
    local l, r = 1, 1
    for i = 2, n do
        if i <= r then z[i] = math.min(r - i + 1, z[i - l + 1]) end
        while i + z[i] <= n and string.byte(s, z[i] + 1) == string.byte(s, i + z[i]) do
            z[i] = z[i] + 1
        end
        if i + z[i] - 1 > r then
            l = i
            r = i + z[i] - 1
        end
    end
    return z
end

if not pcall(debug.getlocal, 4, 1) then
    local z = M.z_algorithm("abacaba")
    local expected = {7, 0, 1, 0, 3, 0, 1}
    assert(#z == #expected, "z length wrong")
    for i = 1, #expected do assert(z[i] == expected[i], "z wrong") end
    print("[Lua ZAlgorithm] Z-algorithm verified")
end

return M
