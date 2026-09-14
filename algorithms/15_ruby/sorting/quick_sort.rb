def quick_sort(arr)
  return arr if arr.length <= 1
  pivot = arr[arr.length / 2]
  less  = arr.select { |x| x < pivot }
  equal = arr.select { |x| x == pivot }
  more  = arr.select { |x| x > pivot }
  quick_sort(less) + equal + quick_sort(more)
end

data = [33, 7, 91, 12, 5, 5, 78, 2, 44, 19]
sorted = quick_sort(data)
raise "not sorted" unless sorted == data.sort
puts "[Ruby QuickSort] Functional quicksort verified: #{sorted.inspect}"
