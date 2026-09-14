local M = {}

function M.manacher(s)
    local t = "#"
    for i = 1, #s do
        t = t .. s:sub(i, i) .. "#"
    end
    local n = #t
    local p = {}
    for i = 1, n do p[i] = 0 end
    local c, r = 0, 0
    for i = 1, n do
        if i <= r then p[i] = math.min(r - i, p[2 * c - i]) end
        while i + p[i] + 1 <= n and i - p[i] - 1 >= 1 and
              string.byte(t, i + p[i] + 1) == string.byte(t, i - p[i] - 1) do
            p[i] = p[i] + 1
        end
        if i + p[i] > r then
            c = i
            r = i + p[i]
        end
    end
    local best = 0
    for i = 1, n do
        if p[i] > best then best = p[i] end
    end
    return best
end

if not pcall(debug.getlocal, 4, 1) then
    assert(M.manacher("abba") == 4, "manacher even wrong")
    assert(M.manacher("racecar") == 7, "manacher odd wrong")
    print("[Lua Manacher] Longest palindromic substring verified")
end

return M
