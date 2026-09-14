module DynamicProgramming

function lis(arr::Vector{T})::Int where T
    isempty(arr) && return 0
    dp = ones(Int, length(arr))
    for i in 2:length(arr)
        for j in 1:(i - 1)
            if arr[j] < arr[i]
                dp[i] = max(dp[i], dp[j] + 1)
            end
        end
    end
    return maximum(dp)
end

end

@assert DynamicProgramming.lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
@assert DynamicProgramming.lis([]) == 0
println("[Julia LIS] Longest increasing subsequence verified")
