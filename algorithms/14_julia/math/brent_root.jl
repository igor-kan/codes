# Brent's Method for Root Finding in Julia (Numerical Recipes 3rd Ed. Chapter 9.3)

function brent_root(f, a::Float64, b::Float64, tol=1e-10, max_iter=100)
    fa = f(a)
    fb = f(b)
    @assert fa * fb <= 0 "Root not bracketed"

    if abs(fa) < abs(fb)
        a, b = b, a
        fa, fb = fb, fa
    end

    c = a
    fc = fa
    mflag = true
    s = b
    d = 0.0

    for _ in 1:max_iter
        if abs(fb) < tol || abs(b - a) < tol
            return b
        end

        if fa != fc && fb != fc
            s = (a * fb * fc) / ((fa - fb) * (fa - fc)) +
                (b * fa * fc) / ((fb - fa) * (fb - fc)) +
                (c * fa * fb) / ((fc - fa) * (fc - fb))
        else
            s = b - fb * (b - a) / (fb - fa)
        end

        c1 = (s - (3 * a + b) / 4) * (s - b) > 0
        c2 = mflag && abs(s - b) >= abs(b - c) / 2
        c3 = !mflag && abs(s - b) >= abs(c - d) / 2

        if c1 || c2 || c3
            s = (a + b) / 2
            mflag = true
        else
            mflag = false
        end

        fs = f(s)
        d = c; c = b; fc = fb
        if fa * fs < 0
            b = s; fb = fs
        else
            a = s; fa = fs
        end

        if abs(fa) < abs(fb)
            a, b = b, a
            fa, fb = fb, fa
        end
    end
    return b
end

r = brent_root(x -> x^2 - 2.0, 0.0, 2.0)
@assert abs(r - sqrt(2.0)) < 1e-6
println("Julia Brent Root Finding verified.")
