-- Rayleigh quotient iteration.
local function rayleigh_quotient(matrix, vector, iterations)
  iterations = iterations or 100
  local n = #matrix
  local x = {}
  local scale = 0
  for i = 1, n do scale = math.max(scale, math.abs(vector[i])) end
  for i = 1, n do x[i] = vector[i] / scale end
  local eigenvalue = 0
  for _ = 1, iterations do
    local product = {}
    for i = 1, n do
      product[i] = 0
      for j = 1, n do product[i] = product[i] + matrix[i][j] * x[j] end
    end
    local norm = 0
    for i = 1, n do norm = math.max(norm, math.abs(product[i])) end
    for i = 1, n do x[i] = product[i] / norm end
    local numerator, denominator = 0, 0
    for i = 1, n do
      local ax = 0
      for j = 1, n do ax = ax + matrix[i][j] * x[j] end
      numerator = numerator + x[i] * ax
      denominator = denominator + x[i] * x[i]
    end
    local next_eigenvalue = numerator / denominator
    if math.abs(next_eigenvalue - eigenvalue) < 1e-12 then return next_eigenvalue, x end
    eigenvalue = next_eigenvalue
  end
  return eigenvalue, x
end

local eigenvalue = rayleigh_quotient({ { 2, 1 }, { 1, 2 } }, { 1, 0 })
assert(math.abs(eigenvalue - 3) < 1e-9, "rayleigh failed")
print("[Lua Rayleigh Quotient] eigenvalue verified")
