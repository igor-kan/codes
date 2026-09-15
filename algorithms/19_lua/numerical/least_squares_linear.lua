-- Ordinary least squares for a straight line.
local function least_squares_linear(xs, ys)
  local n = #xs
  local mean_x, mean_y = 0, 0
  for i = 1, n do mean_x = mean_x + xs[i] / n; mean_y = mean_y + ys[i] / n end
  local numerator, denominator = 0, 0
  for i = 1, n do
    numerator = numerator + (xs[i] - mean_x) * (ys[i] - mean_y)
    denominator = denominator + (xs[i] - mean_x) ^ 2
  end
  local slope = numerator / denominator
  return mean_y - slope * mean_x, slope
end

local intercept, slope = least_squares_linear({ 0, 1, 2, 3 }, { 1, 3, 5, 7 })
assert(math.abs(intercept - 1) < 1e-12 and math.abs(slope - 2) < 1e-12, "least squares failed")
print("[Lua Least Squares Linear] fit verified")
