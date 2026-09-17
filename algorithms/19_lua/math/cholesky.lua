-- Cholesky LL^T in Lua (Numerical Recipes 3rd Ed. Chapter 2.6)

local function cholesky(A)
    local n = #A
    local L = {}
    for i = 1, n do
        L[i] = {}
        for j = 1, n do L[i][j] = 0.0 end
    end

    for i = 1, n do
        for j = 1, i do
            local sum = 0.0
            for k = 1, j - 1 do
                sum = sum + L[i][k] * L[j][k]
            end
            if i == j then
                local val = A[i][i] - sum
                assert(val > 0, "Not positive definite")
                L[i][j] = math.sqrt(val)
            else
                L[i][j] = (A[i][j] - sum) / L[j][j]
            end
        end
    end
    return L
end

local A = {
    {4.0, 12.0, -16.0},
    {12.0, 37.0, -43.0},
    {-16.0, -43.0, 98.0}
}
local L = cholesky(A)
assert(math.abs(L[1][1] - 2.0) < 1e-6)
print("Lua Cholesky verified.")
