local M = {}

function M.gcd(a, b)
    while b ~= 0 do
        a, b = b, a % b
    end
    return a
end

function M.lcm(a, b)
    return math.floor((a / M.gcd(a, b)) * b)
end

return M
