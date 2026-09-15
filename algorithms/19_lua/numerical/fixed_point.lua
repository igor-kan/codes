-- Fixed-point iteration (Numerical Recipes 9.5).
local function fixed_point(g, x, tolerance, max_iterations)
  tolerance = tolerance or 1e-12
  max_iterations = max_iterations or 200
  for _ = 1, max_iterations do
    local nxt = g(x)
    if math.abs(nxt - x) < tolerance then return nxt end
    x = nxt
  end
  return x
end

local root = fixed_point(function(x) return 0.5 * (x + 2 / x) end, 1)
assert(math.abs(root - math.sqrt(2)) < 1e-9, "fixed point failed")
print("[Lua Fixed Point] sqrt(2) verified")
