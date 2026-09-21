module RandomWalkHitting
export expected_hitting_time_1d

function expected_hitting_time_1d(a::Int, b::Int)
    # Symmetric 1D random walk hitting time between -a and b starting at 0: a * b
    return a * b
end
end
