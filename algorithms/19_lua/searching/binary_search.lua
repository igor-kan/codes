local M = {}

function M.binary_search(arr, target)
    local lo, hi = 1, #arr
    while lo <= hi do
        local mid = math.floor((lo + hi) / 2)
        if arr[mid] == target then
            return mid
        elseif arr[mid] < target then
            lo = mid + 1
        else
            hi = mid - 1
        end
    end
    return -1
end

if not pcall(debug.getlocal, 4, 1) then
    local arr = {1, 3, 5, 7, 9, 11, 13}
    assert(M.binary_search(arr, 7) == 4, "found wrong")
    assert(M.binary_search(arr, 8) == -1, "missing wrong")
    assert(M.binary_search(arr, 1) == 1, "left edge wrong")
    print("[Lua BinarySearch] Binary search verified")
end

return M
