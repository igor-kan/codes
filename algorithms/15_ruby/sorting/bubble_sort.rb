def bubble_sort(arr)
  a = arr.dup
  n = a.length
  n.times { |i| (n-i-1).times { |j| a[j], a[j+1] = a[j+1], a[j] if a[j] > a[j+1] } }
  a
end