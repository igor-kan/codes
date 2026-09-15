-- Neville's algorithm for polynomial interpolation.
local function neville_interpolation(xs, ys, x)
  local n = #xs
  local table_ = {}
  for i = 1, n do table_[i] = ys[i] end
  for k = 1, n - 1 do
    for i = 1, n - k do
      table_[i] = ((x - xs[i + k]) * table_[i] + (xs[i] - x) * table_[i + 1]) / (xs[i] - xs[i + k])
    end
  end
  return table_[1]
end

local value = neville_interpolation({ 0, 1, 2 }, { 1, 3, 2 }, 1.5)
assert(math.abs(value - 2.875) < 1e-12, "neville failed")
print("[Lua Neville Interpolation] verified")
