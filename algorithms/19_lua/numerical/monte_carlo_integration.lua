-- Monte Carlo integration.
local function monte_carlo_integration(f, a, b, samples, seed)
  samples = samples or 100000
  seed = seed or 42
  local state = seed
  local modulus = 2 ^ 31
  local total = 0
  for _ = 1, samples do
    state = (1103515245 * state + 12345) % modulus
    total = total + f(a + (b - a) * (state / modulus))
  end
  return (b - a) * total / samples
end

local estimate = monte_carlo_integration(function(x) return x * x end, 0, 1)
assert(math.abs(estimate - 1 / 3) < 0.01, "monte carlo failed")
print("[Lua Monte Carlo Integration] verified")
