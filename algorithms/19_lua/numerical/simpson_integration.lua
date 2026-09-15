-- Composite Simpson's rule (Numerical Recipes 4.1).
local function simpson(f, a, b, n)
  n = n or 1000
  if n % 2 == 1 then n = n + 1 end
  local h = (b - a) / n
  local total = f(a) + f(b)
  for i = 1, n - 1 do
    total = total + (i % 2 == 1 and 4 or 2) * f(a + i * h)
  end
  return total * h / 3
end

local value = simpson(function(x) return x * x end, 0, 1)
assert(math.abs(value - 1 / 3) < 1e-12, "simpson failed")
print("[Lua Simpson Integration] integral verified")
