module Sorting

function selection_sort!(arr::Vector{T}) where T
    n = length(arr)
    for i in 1:(n - 1)
        min_idx = i
        for j in (i + 1):n
            if arr[j] < arr[min_idx]
                min_idx = j
            end
        end
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    end
    return arr
end

selection_sort(arr::Vector{T}) where T = selection_sort!(copy(arr))

end

data = [33, 7, 91, 12, 5, 5, 78, 2, 44, 19]
sorted = Sorting.selection_sort(data)
@assert sorted == sort(data)
println("[Julia SelectionSort] Selection sort verified: ", sorted)
