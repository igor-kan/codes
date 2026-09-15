-- Composite Simpson's 3/8 rule.
local function simpson_38(f, a, b, n)
  if n % 3 ~= 0 then n = n + 3 - n % 3 end
  local h = (b - a) / n
  local total = f(a) + f(b)
  for i = 1, n - 1 do
    total = total + (i % 3 ~= 0 and 3 or 2) * f(a + i * h)
  end
  return 3 * h / 8 * total
end

local value = simpson_38(function(x) return x * x end, 0, 1, 999)
assert(math.abs(value - 1 / 3) < 1e-12, "simpson 3/8 failed")
print("[Lua Simpson 3/8] integral verified")
