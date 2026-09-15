-- Greedy set cover.
local function set_cover(universe, subsets)
  local covered = {}
  local remaining = 0
  for _ in pairs(universe) do remaining = remaining + 1 end
  local chosen = {}
  while remaining > 0 do
    local best, best_count = nil, 0
    for _, subset in ipairs(subsets) do
      local count = 0
      for value in pairs(subset) do
        if universe[value] and not covered[value] then count = count + 1 end
      end
      if count > best_count then best, best_count = subset, count end
    end
    if not best then break end
    chosen[#chosen + 1] = best
    for value in pairs(best) do
      if not covered[value] then covered[value] = true; remaining = remaining - 1 end
    end
  end
  return chosen
end

local chosen = set_cover({ [1] = true, [2] = true, [3] = true, [4] = true, [5] = true },
  { { [1] = true, [2] = true, [3] = true }, { [2] = true, [4] = true },
    { [3] = true, [4] = true }, { [4] = true, [5] = true } })
assert(#chosen == 2, "set cover failed")
print("[Lua Set Cover] greedy cover verified")
