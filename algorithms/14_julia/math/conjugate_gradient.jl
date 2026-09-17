# Conjugate Gradient Linear Solver in Julia (Numerical Recipes 3rd Ed. Chapter 2.7)

function conjugate_gradient(A::Matrix{Float64}, b::Vector{Float64}, tol=1e-8, max_iter=50)
    n = length(b)
    x = zeros(Float64, n)
    r = copy(b)
    p = copy(r)
    rs_old = sum(r .^ 2)

    for _ in 1:max_iter
        if sqrt(rs_old) < tol
            break
        end
        Ap = A * p
        alpha = rs_old / sum(p .* Ap)
        x .+= alpha .* p
        r .-= alpha .* Ap
        rs_new = sum(r .^ 2)
        p .= r .+ (rs_new / rs_old) .* p
        rs_old = rs_new
    end
    return x
end

A = [4.0 1.0; 1.0 3.0]
b = [1.0, 2.0]
x = conjugate_gradient(A, b)
@assert abs(x[1] - 1.0 / 11.0) < 1e-5
println("Julia Conjugate Gradient verified.")
