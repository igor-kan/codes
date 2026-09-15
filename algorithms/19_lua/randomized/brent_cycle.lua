-- Brent's cycle detection.
local function brent_cycle(link, start)
  local power, lam = 1, 1
  local tortoise, hare = start, link[start]
  while tortoise ~= hare do
    if power == lam then tortoise = hare; power = power * 2; lam = 0 end
    hare = link[hare]
    lam = lam + 1
  end
  tortoise, hare = start, start
  for _ = 1, lam do hare = link[hare] end
  local mu = 0
  while tortoise ~= hare do tortoise = link[tortoise]; hare = link[hare]; mu = mu + 1 end
  return mu, lam
end

local link = { 2, 3, 4, 5, 4 }
local mu, lam = brent_cycle(link, 1)
assert(mu == 3 and lam == 2, "brent cycle failed")
print("[Lua Brent Cycle] cycle entry and length verified")
