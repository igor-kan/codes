local M = {}

function M.lis(arr)
    local n = #arr
    if n == 0 then return 0 end
    local dp = {}
    for i = 1, n do dp[i] = 1 end
    for i = 2, n do
        for j = 1, i - 1 do
            if arr[j] < arr[i] then
                dp[i] = math.max(dp[i], dp[j] + 1)
            end
        end
    end
    local best = 0
    for i = 1, n do
        if dp[i] > best then best = dp[i] end
    end
    return best
end

if not pcall(debug.getlocal, 4, 1) then
    assert(M.lis({10, 9, 2, 5, 3, 7, 101, 18}) == 4, "lis wrong")
    assert(M.lis({}) == 0, "lis empty wrong")
    print("[Lua LIS] Longest increasing subsequence verified")
end

return M
