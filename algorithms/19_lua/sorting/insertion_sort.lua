local M = {}

function M.insertion_sort(arr)
    local a = {}
    for i = 1, #arr do a[i] = arr[i] end
    for i = 2, #a do
        local key = a[i]
        local j = i - 1
        while j >= 1 and a[j] > key do
            a[j + 1] = a[j]
            j = j - 1
        end
        a[j + 1] = key
    end
    return a
end

if not pcall(debug.getlocal, 4, 1) then
    local data = {33, 7, 91, 12, 5, 5, 78, 2, 44, 19}
    local sorted = M.insertion_sort(data)
    local expected = {2, 5, 5, 7, 12, 19, 33, 44, 78, 91}
    for i = 1, #expected do assert(sorted[i] == expected[i], "not sorted") end
    print("[Lua InsertionSort] Insertion sort verified: " .. table.concat(sorted, ", "))
end

return M
