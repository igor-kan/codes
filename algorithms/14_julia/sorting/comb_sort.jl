function comb_sort!(arr::Vector{Int})
    n = length(arr)
    gap = n
    shrink = 1.3
    sorted = false
    while !sorted
        gap = floor(Int, gap / shrink)
        if gap <= 1
            gap = 1
            sorted = true
        end
        for i in 1:(n - gap)
            if arr[i] > arr[i + gap]
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = false
            end
        end
    end
    return arr
end
a = [8, 4, 1, 56, 3]
comb_sort!(a)
@assert a == [1, 3, 4, 8, 56]
println("Julia Comb Sort verified.")
