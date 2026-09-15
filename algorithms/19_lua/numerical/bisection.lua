-- Bisection root finding (Numerical Recipes 9.1).
local function bisection(f, a, b, tolerance, max_iterations)
  tolerance = tolerance or 1e-12
  max_iterations = max_iterations or 200
  local fa, fb = f(a), f(b)
  if fa * fb > 0 then error("root is not bracketed") end
  local c = a
  for _ = 1, max_iterations do
    c = 0.5 * (a + b)
    local fc = f(c)
    if fc == 0 or (b - a) / 2 < tolerance then return c end
    if fa * fc < 0 then b, fb = c, fc else a, fa = c, fc end
  end
  return c
end

local root = bisection(function(x) return x * x - 2 end, 0, 2)
assert(math.abs(root - math.sqrt(2)) < 1e-9, "bisection failed")
print("[Lua Bisection] sqrt(2) verified")
