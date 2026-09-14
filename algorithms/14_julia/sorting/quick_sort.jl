module Sorting

function quick_sort(arr::AbstractVector{T}) where T
    if length(arr) <= 1
        return copy(arr)
    end
    pivot = arr[div(length(arr), 2) + 1]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    more = [x for x in arr if x > pivot]
    return vcat(quick_sort(less), equal, quick_sort(more))
end

end

data = [33, 7, 91, 12, 5, 5, 78, 2, 44, 19]
sorted = Sorting.quick_sort(data)
@assert sort(data) == sorted
println("[Julia QuickSort] Functional quicksort verified: ", sorted)
