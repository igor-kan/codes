-- Piecewise linear interpolation.
local function linear_interpolation(xs, ys, x)
  if x <= xs[1] then return ys[1] end
  if x >= xs[#xs] then return ys[#ys] end
  for i = 2, #xs do
    if x <= xs[i] then
      local slope = (ys[i] - ys[i - 1]) / (xs[i] - xs[i - 1])
      return ys[i - 1] + slope * (x - xs[i - 1])
    end
  end
  return ys[#ys]
end

assert(math.abs(linear_interpolation({ 0, 1, 2 }, { 0, 2, 4 }, 0.5) - 1) < 1e-12, "linear failed")
assert(math.abs(linear_interpolation({ 0, 1, 4 }, { 0, 1, 2 }, 2.5) - 1.5) < 1e-12, "linear segment failed")
print("[Lua Linear Interpolation] verified")
