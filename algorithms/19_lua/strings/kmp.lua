local M = {}

function M.compute_lps(pattern)
    local m = #pattern
    local lps = {}
    for i = 1, m do lps[i] = 0 end
    local len = 0
    local i = 2
    while i <= m do
        if pattern:sub(i, i) == pattern:sub(len + 1, len + 1) then
            len = len + 1
            lps[i] = len
            i = i + 1
        else
            if len > 0 then
                len = lps[len]
            else
                lps[i] = 0
                i = i + 1
            end
        end
    end
    return lps
end

function M.kmp_search(text, pattern)
    local n, m = #text, #pattern
    if m == 0 then return {0} end
    local lps = M.compute_lps(pattern)
    local result = {}
    local i, j = 1, 1
    while i <= n do
        if pattern:sub(j, j) == text:sub(i, i) then
            i = i + 1
            j = j + 1
        end
        if j == m + 1 then
            table.insert(result, i - j + 1)
            j = lps[j - 1] + 1
        elseif i <= n and pattern:sub(j, j) ~= text:sub(i, i) then
            if j > 1 then
                j = lps[j - 1] + 1
            else
                i = i + 1
            end
        end
    end
    return result
end

if not pcall(debug.getlocal, 4, 1) then
    print("[Lua KMP] Testing KMP string matching")
    local function tbl_eq(a, b)
        if #a ~= #b then return false end
        for i = 1, #a do if a[i] ~= b[i] then return false end end
        return true
    end
    local r = M.kmp_search("ABABDABACDABABCABAB", "ABABCABAB")
    print("Pattern found at: " .. table.concat(r, " ") .. " (expected 11)")
    r = M.kmp_search("AAAA", "AA")
    print("Pattern found at: " .. table.concat(r, " ") .. " (expected 1 2 3)")
    r = M.kmp_search("HELLO WORLD", "WORLD")
    print("Pattern found at: " .. table.concat(r, " ") .. " (expected 7)")
    print("[Lua KMP] Test completed.")
end

return M