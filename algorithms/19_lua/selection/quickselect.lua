-- Quickselect: expected linear-time order statistic (CLRS 9.2).
local function quickselect(values, k)
  local a = {}
  for i = 1, #values do a[i] = values[i] end
  local lo, hi = 1, #a
  while true do
    local pivot, i = a[hi], lo
    for j = lo, hi - 1 do
      if a[j] < pivot then
        a[i], a[j] = a[j], a[i]
        i = i + 1
      end
    end
    a[i], a[hi] = a[hi], a[i]
    if i == k then return a[i] end
    if k < i then hi = i - 1 else lo = i + 1 end
  end
end

local data = { 3, 2, 1, 5, 6, 4 }
local sorted = { 1, 2, 3, 4, 5, 6 }
for k = 1, #data do
  assert(quickselect(data, k) == sorted[k], "quickselect failed")
end
print("[Lua Quickselect] order statistics verified")
