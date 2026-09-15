# Binary max-heap.
def push_heap(a, value)
  a << value
  i = a.length - 1
  while i > 0
    p = (i - 1) / 2
    break if a[p] >= a[i]

    a[p], a[i] = a[i], a[p]
    i = p
  end
end

def pop_heap(a)
  top = a[0]
  last = a.pop
  unless a.empty?
    a[0] = last
    i = 0
    loop do
      l = 2 * i + 1
      r = 2 * i + 2
      b = i
      b = l if l < a.length && a[l] > a[b]
      b = r if r < a.length && a[r] > a[b]
      break if b == i

      a[i], a[b] = a[b], a[i]
      i = b
    end
  end
  top
end

heap = []
[5, 3, 8, 1, 4].each { |v| push_heap(heap, v) }
previous = Float::INFINITY
until heap.empty?
  x = pop_heap(heap)
  raise "not a max-heap order" if x > previous

  previous = x
end
puts "max heap ok"
