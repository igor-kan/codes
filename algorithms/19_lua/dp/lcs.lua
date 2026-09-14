local M = {}

function M.lcs(s1, s2)
    local m, n = #s1, #s2
    local dp = {}
    for i = 0, m do
        dp[i] = {}
        for j = 0, n do dp[i][j] = 0 end
    end

    for i = 1, m do
        for j = 1, n do
            if s1:sub(i, i) == s2:sub(j, j) then
                dp[i][j] = dp[i - 1][j - 1] + 1
            else
                dp[i][j] = math.max(dp[i - 1][j], dp[i][j - 1])
            end
        end
    end
    return dp[m][n]
end

return M
