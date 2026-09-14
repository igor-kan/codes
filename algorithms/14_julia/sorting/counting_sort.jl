module Sorting

function counting_sort(arr::Vector{Int})::Vector{Int}
    isempty(arr) && return Int[]
    max_val = maximum(arr)
    count = zeros(Int, max_val + 1)
    for x in arr
        count[x + 1] += 1
    end
    for i in 2:(max_val + 1)
        count[i] += count[i - 1]
    end
    out = Vector{Int}(undef, length(arr))
    for x in Iterators.reverse(arr)
        count[x + 1] -= 1
        out[count[x + 1] + 1] = x
    end
    return out
end

end

data = [4, 2, 2, 8, 3, 3, 1]
sorted = Sorting.counting_sort(data)
@assert sorted == sort(data)
println("[Julia CountingSort] Counting sort verified: ", sorted)
