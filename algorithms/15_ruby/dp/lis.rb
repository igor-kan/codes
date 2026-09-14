def lis(arr)
  return 0 if arr.empty?
  dp = Array.new(arr.length, 1)
  (1...arr.length).each do |i|
    (0...i).each do |j|
      dp[i] = [dp[i], dp[j] + 1].max if arr[j] < arr[i]
    end
  end
  dp.max
end

raise "lis wrong" unless lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
raise "lis empty wrong" unless lis([]) == 0
puts "[Ruby LIS] Longest increasing subsequence verified"
