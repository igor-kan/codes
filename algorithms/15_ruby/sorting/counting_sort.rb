def counting_sort(arr)
  return arr.dup if arr.empty?
  max = arr.max
  count = Array.new(max + 1, 0)
  arr.each { |x| count[x] += 1 }
  (1..max).each { |i| count[i] += count[i - 1] }
  out = Array.new(arr.length)
  arr.reverse_each do |x|
    count[x] -= 1
    out[count[x]] = x
  end
  out
end

data = [4, 2, 2, 8, 3, 3, 1]
sorted = counting_sort(data)
raise "not sorted" unless sorted == data.sort
puts "[Ruby CountingSort] Counting sort verified: #{sorted.inspect}"
