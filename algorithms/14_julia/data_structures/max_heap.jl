# Binary max-heap.

function push_heap!(a::Vector{Int}, v::Int)
    push!(a, v)
    i = length(a)
    while i > 1
        p = i ÷ 2
        a[p] >= a[i] && break
        a[p], a[i] = a[i], a[p]
        i = p
    end
end

function pop_heap!(a::Vector{Int})
    top = a[1]
    last = pop!(a)
    if !isempty(a)
        a[1] = last
        i = 1
        while true
            l, r, b = 2i, 2i + 1, i
            l <= length(a) && a[l] > a[b] && (b = l)
            r <= length(a) && a[r] > a[b] && (b = r)
            b == i && break
            a[i], a[b] = a[b], a[i]
            i = b
        end
    end
    top
end

a = Int[]
for v in [5, 3, 8, 1, 4]
    push_heap!(a, v)
end
prev = typemax(Int)
while !isempty(a)
    x = pop_heap!(a)
    @assert x <= prev
    global prev = x
end
println("max heap ok")
