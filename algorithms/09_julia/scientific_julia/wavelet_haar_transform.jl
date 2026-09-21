module HaarWavelet
export haar_step

function haar_step(signal::Vector{Float64})
    n = length(signal)
    approx = zeros(div(n, 2))
    detail = zeros(div(n, 2))
    for i in 1:div(n, 2)
        approx[i] = (signal[2*i - 1] + signal[2*i]) / sqrt(2.0)
        detail[i] = (signal[2*i - 1] - signal[2*i]) / sqrt(2.0)
    end
    return approx, detail
end
end
