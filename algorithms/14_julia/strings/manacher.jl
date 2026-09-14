module Strings

function manacher(s::AbstractString)::Int
    t = "#" * join(collect(s), "#") * "#"
    n = length(t)
    p = zeros(Int, n)
    c, r = 0, 0
    for i in 1:n
        if i <= r
            p[i] = min(r - i, p[2 * c - i])
        end
        while i + p[i] + 1 <= n && i - p[i] - 1 >= 1 &&
              t[i + p[i] + 1] == t[i - p[i] - 1]
            p[i] += 1
        end
        if i + p[i] > r
            c = i
            r = i + p[i]
        end
    end
    return maximum(p)
end

end

@assert Strings.manacher("abba") == 4
@assert Strings.manacher("racecar") == 7
println("[Julia Manacher] Longest palindromic substring verified")
