local M = {}

function M.kadane(arr)
    local best = arr[1]
    local cur = arr[1]
    for i = 2, #arr do
        cur = math.max(arr[i], cur + arr[i])
        best = math.max(best, cur)
    end
    return best
end

if not pcall(debug.getlocal, 4, 1) then
    assert(M.kadane({-2, 1, -3, 4, -1, 2, 1, -5, 4}) == 6, "kadane wrong")
    assert(M.kadane({-5, -2, -3}) == -2, "kadane all-negative wrong")
    print("[Lua Kadane] Maximum subarray sum verified")
end

return M
