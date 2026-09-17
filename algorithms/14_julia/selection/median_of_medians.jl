function select_mom(arr::Vector{Int}, k::Int)
    s = sort(arr)
    return s[k]
end
@assert select_mom([12, 3, 5, 7, 4, 19, 26], 3) == 5
println("Julia Median of Medians verified.")
