module Searching

function binary_search(arr::Vector{T}, target::T)::Int where T
    lo, hi = 1, length(arr)
    while lo <= hi
        mid = div(lo + hi, 2)
        if arr[mid] == target
            return mid
        elseif arr[mid] < target
            lo = mid + 1
        else
            hi = mid - 1
        end
    end
    return -1
end

end

arr = [1, 3, 5, 7, 9, 11, 13]
@assert Searching.binary_search(arr, 7) == 4
@assert Searching.binary_search(arr, 8) == -1
@assert Searching.binary_search(arr, 1) == 1
println("[Julia BinarySearch] Binary search verified")
