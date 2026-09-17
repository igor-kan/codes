function rabin_karp(text::String, pat::String)
    matches = Int[]
    n, m = length(text), length(pat)
    if m == 0 || m > n return matches end
    d, q = 256, 1000000007
    h = powermod(d, m - 1, q)
    p_hash, t_hash = 0, 0
    for i in 1:m
        p_hash = (d * p_hash + Int(pat[i])) % q
        t_hash = (d * t_hash + Int(text[i])) % q
    end
    for i in 1:(n - m + 1)
        if p_hash == t_hash && text[i:i + m - 1] == pat
            push!(matches, i)
        end
        if i <= n - m
            t_hash = (d * (t_hash - Int(text[i]) * h) + Int(text[i + m])) % q
            t_hash = (t_hash + q) % q
        end
    end
    return matches
end
m = rabin_karp("GEEKS FOR GEEKS", "GEEK")
@assert !isempty(m)
println("Julia Rabin-Karp verified.")
