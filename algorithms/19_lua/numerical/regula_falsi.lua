-- Regula falsi root finding (Numerical Recipes 9.2).
local function regula_falsi(f, a, b, tolerance, max_iterations)
  tolerance = tolerance or 1e-12
  max_iterations = max_iterations or 200
  local fa, fb = f(a), f(b)
  if fa * fb > 0 then error("root is not bracketed") end
  local c = a
  for _ = 1, max_iterations do
    c = (a * fb - b * fa) / (fb - fa)
    local fc = f(c)
    if math.abs(fc) < tolerance then return c end
    if fa * fc < 0 then b, fb = c, fc else a, fa = c, fc end
  end
  return c
end

local root = regula_falsi(function(x) return x * x - 2 end, 0, 2)
assert(math.abs(root - math.sqrt(2)) < 1e-9, "regula falsi failed")
print("[Lua Regula Falsi] sqrt(2) verified")
