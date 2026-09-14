module MathUtils

function extended_gcd(a::Integer, b::Integer)
    if b == 0
        return a, 1, 0
    end
    g, x1, y1 = extended_gcd(b, mod(a, b))
    x = y1
    y = x1 - div(a, b) * y1
    return g, x, y
end

lcm_custom(a::Integer, b::Integer) = div(abs(a * b), gcd(a, b))

end
