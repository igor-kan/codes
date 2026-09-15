# Boyer-Moore-Horspool substring search.

function boyer_moore(text::String, pat::String)
    n, m = length(text), length(pat)
    skip = fill(m, 256)
    for i in 1:(m - 1)
        skip[Int(pat[i]) + 1] = m - i
    end
    i = 1
    while i + m - 1 <= n
        j = m
        while j >= 1 && text[i + j - 1] == pat[j]
            j -= 1
        end
        j == 0 && return i - 1
        i += skip[Int(text[i + m - 1]) + 1]
    end
    return -1
end

@assert boyer_moore("here is a simple example", "example") == 17
@assert boyer_moore("abc", "xyz") == -1
println("boyer-moore ok")
