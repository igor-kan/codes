def z_algorithm(s)
  n = s.length
  z = Array.new(n, 0)
  z[0] = n
  l = r = 0
  (1...n).each do |i|
    z[i] = [r - i + 1, z[i - l]].min if i <= r
    while i + z[i] < n && s[z[i]] == s[i + z[i]]
      z[i] += 1
    end
    if i + z[i] - 1 > r
      l = i
      r = i + z[i] - 1
    end
  end
  z
end

raise "z-algorithm wrong" unless z_algorithm("abacaba") == [7, 0, 1, 0, 3, 0, 1]
puts "[Ruby ZAlgorithm] Z-algorithm verified"
