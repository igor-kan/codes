def kadane(arr)
  best = cur = arr[0]
  arr[1..].each do |x|
    cur = [x, cur + x].max
    best = [best, cur].max
  end
  best
end

raise "kadane wrong" unless kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
raise "kadane all negative wrong" unless kadane([-5, -2, -3]) == -2
puts "[Ruby Kadane] Maximum subarray sum verified"
