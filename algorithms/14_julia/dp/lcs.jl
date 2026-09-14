module DynamicProgramming

function lcs(a::AbstractString, b::AbstractString)::Int
    m, n = length(a), length(b)
    dp = zeros(Int, m + 1, n + 1)
    
    a_chars, b_chars = collect(a), collect(b)
    for i in 1:m
        for j in 1:n
            if a_chars[i] == b_chars[j]
                dp[i + 1, j + 1] = dp[i, j] + 1
            else
                dp[i + 1, j + 1] = max(dp[i + 1, j], dp[i, j + 1])
            end
        end
    end
    return dp[m + 1, n + 1]
end

end
