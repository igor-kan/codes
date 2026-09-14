module Strings

function z_algorithm(s::AbstractString)::Vector{Int}
    n = length(s)
    z = zeros(Int, n)
    z[1] = n
    l, r = 1, 1
    for i in 2:n
        if i <= r
            z[i] = min(r - i + 1, z[i - l + 1])
        end
        while i + z[i] <= n && s[z[i] + 1] == s[i + z[i]]
            z[i] += 1
        end
        if i + z[i] - 1 > r
            l = i
            r = i + z[i] - 1
        end
    end
    return z
end

end

@assert Strings.z_algorithm("abacaba") == [7, 0, 1, 0, 3, 0, 1]
println("[Julia ZAlgorithm] Z-algorithm verified")
