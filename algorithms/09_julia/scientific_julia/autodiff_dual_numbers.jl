module AutoDiffDual
export Dual, dual_deriv

struct Dual
    val::Float64
    eps::Float64
end

Base.:+(a::Dual, b::Dual) = Dual(a.val + b.val, a.eps + b.eps)
Base.:*(a::Dual, b::Dual) = Dual(a.val * b.val, a.val * b.eps + a.eps * b.val)

function dual_deriv(f, x::Float64)
    res = f(Dual(x, 1.0))
    return res.eps
end
end
