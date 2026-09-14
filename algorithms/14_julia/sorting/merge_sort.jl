module Sorting

function merge_sort(arr::AbstractVector{T}) where T
    if length(arr) <= 1
        return copy(arr)
    end
    mid = div(length(arr), 2)
    left = merge_sort(@view arr[1:mid])
    right = merge_sort(@view arr[mid+1:end])
    return merge_arrays(left, right)
end

function merge_arrays(left::Vector{T}, right::Vector{T}) where T
    res = Vector{T}()
    sizehint!(res, length(left) + length(right))
    i, j = 1, 1
    while i <= length(left) && j <= length(right)
        if left[i] <= right[j]
            push!(res, left[i]); i += 1
        else
            push!(res, right[j]); j += 1
        end
    end
    append!(res, @view left[i:end])
    append!(res, @view right[j:end])
    return res
end

end
