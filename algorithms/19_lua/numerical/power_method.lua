-- Power iteration for the dominant eigenvalue.
local function power_method(matrix)
  local n = #matrix
  local vector = {}
  for i = 1, n do vector[i] = 1 end
  local eigenvalue = 0
  for _ = 1, 1000 do
    local product = {}
    for i = 1, n do
      local total = 0
      for j = 1, n do total = total + matrix[i][j] * vector[j] end
      product[i] = total
    end
    local norm = 0
    for i = 1, n do norm = math.max(norm, math.abs(product[i])) end
    for i = 1, n do vector[i] = product[i] / norm end
    if math.abs(norm - eigenvalue) < 1e-12 then eigenvalue = norm break end
    eigenvalue = norm
  end
  return eigenvalue, vector
end

local matrix = { { 4, 1 }, { 2, 3 } }
local eigenvalue, vector = power_method(matrix)
assert(math.abs(eigenvalue - 5) < 1e-9, "power method failed")
for i = 1, 2 do
  local av = matrix[i][1] * vector[1] + matrix[i][2] * vector[2]
  assert(math.abs(av - eigenvalue * vector[i]) < 1e-9, "eigenvector failed")
end
print("[Lua Power Method] dominant eigenvalue verified")
