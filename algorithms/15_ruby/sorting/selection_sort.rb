def selection_sort(arr)
  a = arr.dup
  (0...a.length).each do |i|
    min_idx = i
    (i + 1...a.length).each { |j| min_idx = j if a[j] < a[min_idx] }
    a[i], a[min_idx] = a[min_idx], a[i]
  end
  a
end

data = [33, 7, 91, 12, 5, 5, 78, 2, 44, 19]
sorted = selection_sort(data)
raise "not sorted" unless sorted == data.sort
puts "[Ruby SelectionSort] Selection sort verified: #{sorted.inspect}"
