def insertion_sort(arr)
  a = arr.dup
  (1...a.length).each do |i|
    key = a[i]
    j = i - 1
    while j >= 0 && a[j] > key
      a[j + 1] = a[j]
      j -= 1
    end
    a[j + 1] = key
  end
  a
end

data = [33, 7, 91, 12, 5, 5, 78, 2, 44, 19]
sorted = insertion_sort(data)
raise "not sorted" unless sorted == data.sort
puts "[Ruby InsertionSort] Insertion sort verified: #{sorted.inspect}"
