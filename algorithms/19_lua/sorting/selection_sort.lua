local M = {}

function M.selection_sort(arr)
    local a = {}
    for i = 1, #arr do a[i] = arr[i] end
    for i = 1, #a - 1 do
        local min_idx = i
        for j = i + 1, #a do
            if a[j] < a[min_idx] then min_idx = j end
        end
        a[i], a[min_idx] = a[min_idx], a[i]
    end
    return a
end

if not pcall(debug.getlocal, 4, 1) then
    local data = {33, 7, 91, 12, 5, 5, 78, 2, 44, 19}
    local sorted = M.selection_sort(data)
    local expected = {2, 5, 5, 7, 12, 19, 33, 44, 78, 91}
    for i = 1, #expected do assert(sorted[i] == expected[i], "not sorted") end
    print("[Lua SelectionSort] Selection sort verified: " .. table.concat(sorted, ", "))
end

return M
