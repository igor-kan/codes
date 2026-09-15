-- Boyer-Moore-Horspool substring search.
local function boyer_moore(text, pat)
  local n, m = #text, #pat
  local skip = {}
  for i = 1, 256 do skip[i] = m end
  for i = 1, m - 1 do skip[pat:byte(i) + 1] = m - i end
  local i = 1
  while i + m - 1 <= n do
    local j = m
    while j >= 1 and text:sub(i + j - 1, i + j - 1) == pat:sub(j, j) do
      j = j - 1
    end
    if j == 0 then return i - 1 end
    i = i + skip[text:byte(i + m - 1) + 1]
  end
  return -1
end

assert(boyer_moore("here is a simple example", "example") == 17)
assert(boyer_moore("abc", "xyz") == -1)
print("boyer-moore ok")
