-- Binary max-heap.
local function push(a, v)
  a[#a + 1] = v
  local i = #a
  while i > 1 do
    local p = math.floor(i / 2)
    if a[p] >= a[i] then break end
    a[p], a[i] = a[i], a[p]
    i = p
  end
end

local function pop(a)
  local top = a[1]
  local last = table.remove(a)
  if #a > 0 then
    a[1] = last
    local i = 1
    while true do
      local l, r, b = 2 * i, 2 * i + 1, i
      if l <= #a and a[l] > a[b] then b = l end
      if r <= #a and a[r] > a[b] then b = r end
      if b == i then break end
      a[i], a[b] = a[b], a[i]
      i = b
    end
  end
  return top
end

local heap = {}
for _, v in ipairs({ 5, 3, 8, 1, 4 }) do push(heap, v) end
local previous = math.huge
while #heap > 0 do
  local x = pop(heap)
  assert(x <= previous, "not a max-heap order")
  previous = x
end
print("max heap ok")
