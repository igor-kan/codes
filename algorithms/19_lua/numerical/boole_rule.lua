-- Composite Boole's rule.
local function boole_rule(f, a, b, n)
  if n % 4 ~= 0 then n = n + 4 - n % 4 end
  local h = (b - a) / n
  local total = 7 * (f(a) + f(b))
  for i = 1, n - 1 do
    if i % 4 == 0 then
      total = total + 14 * f(a + i * h)
    elseif i % 2 == 0 then
      total = total + 12 * f(a + i * h)
    else
      total = total + 32 * f(a + i * h)
    end
  end
  return 2 * h / 45 * total
end

local value = boole_rule(function(x) return x * x end, 0, 1, 998)
assert(math.abs(value - 1 / 3) < 1e-12, "boole rule failed")
print("[Lua Boole Rule] integral verified")
