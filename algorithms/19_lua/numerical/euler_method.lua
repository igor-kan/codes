-- Forward Euler method for ODEs.
local function euler_method(f, y0, t0, t1, steps)
  steps = steps or 1000
  local h = (t1 - t0) / steps
  local y, t = y0, t0
  for _ = 1, steps do
    y = y + h * f(t, y)
    t = t + h
  end
  return y
end

local value = euler_method(function(t, y) return y end, 1, 0, 1)
assert(math.abs(value - math.exp(1)) < 0.01, "euler method failed")
print("[Lua Euler Method] e verified")
