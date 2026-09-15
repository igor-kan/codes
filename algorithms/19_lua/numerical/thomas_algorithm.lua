-- Thomas algorithm for tridiagonal systems.
local function thomas_algorithm(lower, diagonal, upper, rhs)
  local n = #diagonal
  local c, d = {}, {}
  c[1] = upper[1] / diagonal[1]
  d[1] = rhs[1] / diagonal[1]
  for i = 2, n do
    local denominator = diagonal[i] - lower[i] * c[i - 1]
    c[i] = i < n and upper[i] / denominator or 0
    d[i] = (rhs[i] - lower[i] * d[i - 1]) / denominator
  end
  local x = {}
  x[n] = d[n]
  for i = n - 1, 1, -1 do x[i] = d[i] - c[i] * x[i + 1] end
  return x
end

local x = thomas_algorithm({ 0, -1, -1 }, { 2, 2, 2 }, { -1, -1, 0 }, { 1, 0, 1 })
for i = 1, 3 do assert(math.abs(x[i] - 1) < 1e-12, "thomas failed") end
print("[Lua Thomas Algorithm] tridiagonal solve verified")
