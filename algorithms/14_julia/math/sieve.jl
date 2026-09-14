module MathUtils

function sieve(limit::Int)::Vector{Int}
    if limit < 2
        return Int[]
    end
    is_prime = trues(limit)
    is_prime[1] = false
    for p in 2:isqrt(limit)
        if is_prime[p]
            is_prime[p*p:p:limit] .= false
        end
    end
    return findall(is_prime)
end

end
