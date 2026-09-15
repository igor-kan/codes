-- Activity-selection problem (CLRS 16.1).
local function activity_selection(activities)
  table.sort(activities, function(a, b) return a.finish < b.finish end)
  local chosen, last = {}, -math.huge
  for _, activity in ipairs(activities) do
    if activity.start >= last then
      chosen[#chosen + 1] = activity
      last = activity.finish
    end
  end
  return chosen
end

local acts = {
  { start = 1, finish = 4 }, { start = 3, finish = 5 }, { start = 0, finish = 6 },
  { start = 5, finish = 7 }, { start = 3, finish = 9 }, { start = 5, finish = 9 },
  { start = 6, finish = 10 }, { start = 8, finish = 11 }, { start = 8, finish = 12 },
  { start = 2, finish = 14 }, { start = 12, finish = 16 },
}
assert(#activity_selection(acts) == 4, "activity selection failed")
print("[Lua Activity Selection] maximum set verified")
