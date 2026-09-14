local M = {}

function M.knapsack(weights, values, capacity)
    local n = #weights
    local dp = {}
    for i = 0, n do
        dp[i] = {}
        for w = 0, capacity do dp[i][w] = 0 end
    end

    for i = 1, n do
        for w = 0, capacity do
            if weights[i] > w then
                dp[i][w] = dp[i - 1][w]
            else
                dp[i][w] = math.max(dp[i - 1][w], dp[i - 1][w - weights[i]] + values[i])
            end
        end
    end
    return dp[n][capacity]
end

if not pcall(debug.getlocal, 4, 1) then
    print("[Lua Knapsack] Testing 0/1 knapsack")
    local w = {2, 3, 4, 5}
    local v = {3, 4, 5, 6}
    local cap = 8
    local result = M.knapsack(w, v, cap)
    print("Max value: " .. result .. " (expected 10)")
    local w2 = {1, 2, 3}
    local v2 = {10, 15, 40}
    print("Max value (cap=6): " .. M.knapsack(w2, v2, 6) .. " (expected 65)")
    print("[Lua Knapsack] Test completed.")
end

return M