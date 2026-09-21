module MonteCarloIsing
export ising_energy_2d

function ising_energy_2d(spins::Matrix{Int}, J::Float64=1.0)
    n, m = size(spins)
    E = 0.0
    for i in 1:n
        for j in 1:m
            right = spins[i, j == m ? 1 : j + 1]
            down = spins[i == n ? 1 : i + 1, j]
            E -= J * spins[i, j] * (right + down)
        end
    end
    return E
end
end
