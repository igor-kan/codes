-- Aitken's delta-squared acceleration.
local function aitken(x0, x1, x2)
  local denominator = x2 - 2 * x1 + x0
  if math.abs(denominator) < 1e-15 then return x2 end
  return x2 - (x2 - x1) ^ 2 / denominator
end

assert(math.abs(aitken(1, 0.5, 0.25)) < 1e-12, "aitken geometric failed")
local sequence = {}
for n = 0, 2 do sequence[n + 1] = 2 - 2 * 0.5 ^ n end
assert(math.abs(aitken(sequence[1], sequence[2], sequence[3]) - 2) < 1e-12, "aitken failed")
print("[Lua Aitken] acceleration verified")
