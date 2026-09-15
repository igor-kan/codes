-- Velocity Verlet integration.
local function verlet(acceleration, x0, v0, dt, steps)
  local x, v = x0, v0
  for _ = 1, steps do
    local a = acceleration(x)
    local x_new = x + v * dt + 0.5 * a * dt * dt
    local a_new = acceleration(x_new)
    v = v + 0.5 * (a + a_new) * dt
    x = x_new
  end
  return x, v
end

local position, velocity = verlet(function(x) return -x end, 1, 0, 0.001, 10000)
local energy = 0.5 * (velocity * velocity + position * position)
assert(math.abs(energy - 0.5) < 1e-3, "verlet energy failed")
assert(math.abs(position - math.cos(10)) < 1e-2, "verlet position failed")
print("[Lua Verlet] harmonic oscillator verified")
