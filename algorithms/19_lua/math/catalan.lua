-- Catalan numbers by the recurrence.
local c = {}
for i = 1, 11 do c[i] = 0 end
c[1] = 1
for n = 1, 10 do
  local s = 0
  for k = 0, n - 1 do
    s = s + c[k + 1] * c[n - k]
  end
  c[n + 1] = s
end
assert(c[6] == 42 and c[11] == 16796, "wrong Catalan numbers")
print("catalan(10)=" .. c[11])
