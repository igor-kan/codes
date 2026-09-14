local M = {}

function M.counting_sort(arr)
    if #arr == 0 then return {} end
    local max_val = arr[1]
    for i = 2, #arr do
        if arr[i] > max_val then max_val = arr[i] end
    end
    local count = {}
    for i = 1, max_val + 1 do count[i] = 0 end
    for _, x in ipairs(arr) do count[x + 1] = count[x + 1] + 1 end
    for i = 2, max_val + 1 do count[i] = count[i] + count[i - 1] end
    local out = {}
    for i = #arr, 1, -1 do
        local x = arr[i]
        count[x + 1] = count[x + 1] - 1
        out[count[x + 1] + 1] = x
    end
    return out
end

if not pcall(debug.getlocal, 4, 1) then
    local data = {4, 2, 2, 8, 3, 3, 1}
    local sorted = M.counting_sort(data)
    local expected = {1, 2, 2, 3, 3, 4, 8}
    for i = 1, #expected do assert(sorted[i] == expected[i], "not sorted") end
    print("[Lua CountingSort] Counting sort verified: " .. table.concat(sorted, ", "))
end

return M
