local M = {}

local function merge(left, right)
    local result, i, j = {}, 1, 1
    while i <= #left and j <= #right do
        if left[i] <= right[j] then
            table.insert(result, left[i]); i = i + 1
        else
            table.insert(result, right[j]); j = j + 1
        end
    end
    while i <= #left do table.insert(result, left[i]); i = i + 1 end
    while j <= #right do table.insert(result, right[j]); j = j + 1 end
    return result
end

function M.merge_sort(arr)
    if #arr <= 1 then
        return arr
    end
    local mid = math.floor(#arr / 2)
    local left, right = {}, {}
    for i = 1, mid do left[i] = arr[i] end
    for i = mid + 1, #arr do right[i - mid] = arr[i] end
    return merge(M.merge_sort(left), M.merge_sort(right))
end

local function tbl_eq(a, b)
    if #a ~= #b then return false end
    for i = 1, #a do if a[i] ~= b[i] then return false end end
    return true
end

if not pcall(debug.getlocal, 4, 1) then
    local data = {33, 7, 91, 12, 5, 5, 78, 2, 44, 19}
    local sorted = M.merge_sort(data)
    assert(tbl_eq(sorted, {2, 5, 5, 7, 12, 19, 33, 44, 78, 91}), "not sorted")
    print("[Lua MergeSort] Recursive merge sort verified: " .. table.concat(sorted, ", "))
end

return M
