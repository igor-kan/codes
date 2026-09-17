function shell_sort!(arr::Vector{Int})
    n = length(arr)
    h = 1
    while h < div(n, 3)
        h = 3 * h + 1
    end
    while h >= 1
        for i in (h + 1):n
            temp = arr[i]
            j = i
            while j > h && arr[j - h] > temp
                arr[j] = arr[j - h]
                j -= h
            end
            arr[j] = temp
        end
        h = div(h, 3)
    end
    return arr
end
a = [5, 2, 8, 1, 9]
shell_sort!(a)
@assert a == [1, 2, 5, 8, 9]
println("Julia Shell Sort verified.")
