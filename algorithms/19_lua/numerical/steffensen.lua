-- Steffensen's method.
local function steffensen(g, x, tolerance, max_iterations)
  tolerance = tolerance or 1e-12
  max_iterations = max_iterations or 100
  for _ = 1, max_iterations do
    local x1 = g(x)
    local x2 = g(x1)
    local denominator = x2 - 2 * x1 + x
    if math.abs(denominator) < 1e-15 then return x2 end
    local nxt = x - (x1 - x) ^ 2 / denominator
    if math.abs(nxt - x) < tolerance then return nxt end
    x = nxt
  end
  return x
end

local root = steffensen(function(x) return 0.5 * (x + 2 / x) end, 1)
assert(math.abs(root - math.sqrt(2)) < 1e-12, "steffensen failed")
print("[Lua Steffensen] sqrt(2) verified")
