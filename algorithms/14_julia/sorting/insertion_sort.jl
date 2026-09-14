module Sorting

function insertion_sort!(arr::Vector{T}) where T
    for i in 2:length(arr)
        key = arr[i]
        j = i - 1
        while j >= 1 && arr[j] > key
            arr[j + 1] = arr[j]
            j -= 1
        end
        arr[j + 1] = key
    end
    return arr
end

insertion_sort(arr::Vector{T}) where T = insertion_sort!(copy(arr))

end

data = [33, 7, 91, 12, 5, 5, 78, 2, 44, 19]
sorted = Sorting.insertion_sort(data)
@assert sorted == sort(data)
println("[Julia InsertionSort] Insertion sort verified: ", sorted)
