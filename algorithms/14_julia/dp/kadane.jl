module DynamicProgramming

function kadane(arr::Vector{Int})::Int
    best = arr[1]
    cur = arr[1]
    for i in 2:length(arr)
        cur = max(arr[i], cur + arr[i])
        best = max(best, cur)
    end
    return best
end

end

@assert DynamicProgramming.kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
@assert DynamicProgramming.kadane([-5, -2, -3]) == -2
println("[Julia Kadane] Maximum subarray sum verified")
