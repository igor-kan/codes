local M = {}

function M.quick_sort(arr)
    if #arr <= 1 then
        return arr
    end
    local pivot = arr[math.floor(#arr / 2) + 1]
    local less, equal, greater = {}, {}, {}
    for _, v in ipairs(arr) do
        if v < pivot then
            table.insert(less, v)
        elseif v > pivot then
            table.insert(greater, v)
        else
            table.insert(equal, v)
        end
    end
    local result = M.quick_sort(less)
    for _, v in ipairs(equal) do table.insert(result, v) end
    for _, v in ipairs(M.quick_sort(greater)) do table.insert(result, v) end
    return result
end

local function tbl_eq(a, b)
    if #a ~= #b then return false end
    for i = 1, #a do if a[i] ~= b[i] then return false end end
    return true
end

if not pcall(debug.getlocal, 4, 1) then
    local data = {33, 7, 91, 12, 5, 5, 78, 2, 44, 19}
    local sorted = M.quick_sort(data)
    assert(tbl_eq(sorted, {2, 5, 5, 7, 12, 19, 33, 44, 78, 91}), "not sorted")
    print("[Lua QuickSort] Functional quicksort verified: " .. table.concat(sorted, ", "))
end

return M
