module SpectralFFTPDE
export linear_dispersion_wavenumbers

function linear_dispersion_wavenumbers(n::Int, L::Float64)
    k = 2.0 * pi / L .* [0:div(n,2)-1; -div(n,2):-1]
    return k
end
end
