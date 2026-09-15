-- Rod cutting (CLRS 15.1).
local function cut_rod(prices, n)
  local best = {}
  for i = 0, n do best[i] = 0 end
  for length = 1, n do
    for i = 1, length do
      best[length] = math.max(best[length], prices[i] + best[length - i])
    end
  end
  return best[n]
end

local prices = { 1, 5, 8, 9, 10, 17, 17, 20, 24, 30 }
assert(cut_rod(prices, 4) == 10, "rod cutting failed")
assert(cut_rod(prices, 7) == 18, "rod cutting failed")
assert(cut_rod(prices, 10) == 30, "rod cutting failed")
print("[Lua Rod Cutting] optimal revenue verified")
