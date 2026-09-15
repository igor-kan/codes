-- Newton-Raphson root finding (Numerical Recipes 9.4).
local function newton(f, df, x)
  for _ = 1, 100 do
    local fx = f(x)
    if math.abs(fx) < 1e-12 then break end
    x = x - fx / df(x)
  end
  return x
end

local root = newton(function(x) return x * x - 2 end, function(x) return 2 * x end, 1.0)
assert(math.abs(root - math.sqrt(2)) < 1e-9, "newton-raphson failed")
print("[Lua Newton-Raphson] sqrt(2) verified")
