-- Midpoint method for ODEs.
local function midpoint_method(f, y0, t0, t1, steps)
  steps = steps or 1000
  local h = (t1 - t0) / steps
  local y, t = y0, t0
  for _ = 1, steps do
    local k1 = f(t, y)
    local k2 = f(t + h / 2, y + h * k1 / 2)
    y = y + h * k2
    t = t + h
  end
  return y
end

local value = midpoint_method(function(t, y) return y end, 1, 0, 1)
assert(math.abs(value - math.exp(1)) < 1e-4, "midpoint method failed")
print("[Lua Midpoint Method] e verified")
