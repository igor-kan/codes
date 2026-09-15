# Catalan numbers by the recurrence.
c = zeros(Int, 11)
c[1] = 1
for n in 1:10
    s = 0
    for k in 0:(n - 1)
        s += c[k + 1] * c[n - k]
    end
    c[n + 1] = s
end
@assert c[6] == 42 && c[11] == 16796
println("catalan(10)=", c[11])
