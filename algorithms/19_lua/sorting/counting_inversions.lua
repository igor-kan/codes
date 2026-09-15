-- Count inversions with a modified merge sort (CLRS 2.4 style).
local function merge_count(a, buf, lo, hi)
  if hi - lo <= 1 then return 0 end
  local mid = math.floor((lo + hi) / 2)
  local inversions = merge_count(a, buf, lo, mid) + merge_count(a, buf, mid, hi)
  local i, j, k = lo, mid, lo
  while i < mid and j < hi do
    if a[i] <= a[j] then
      buf[k] = a[i]; i = i + 1
    else
      buf[k] = a[j]; j = j + 1; inversions = inversions + mid - i
    end
    k = k + 1
  end
  while i < mid do buf[k] = a[i]; i = i + 1; k = k + 1 end
  while j < hi do buf[k] = a[j]; j = j + 1; k = k + 1 end
  for t = lo, hi - 1 do a[t] = buf[t] end
  return inversions
end

local function count_inversions(values)
  local a = {}
  for i = 1, #values do a[i] = values[i] end
  return merge_count(a, {}, 1, #a + 1)
end

assert(count_inversions({ 2, 4, 1, 3, 5 }) == 3, "inversion count failed")
assert(count_inversions({ 5, 4, 3, 2, 1 }) == 10, "reverse inversion count failed")
print("[Lua Counting Inversions] merge-sort count verified")
