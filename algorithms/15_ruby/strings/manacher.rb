def manacher(s)
  t = "#" + s.chars.join("#") + "#"
  n = t.length
  p = Array.new(n, 0)
  c = r = 0
  (0...n).each do |i|
    p[i] = [r - i, p[2 * c - i]].min if i < r
    while i + p[i] + 1 < n && i - p[i] - 1 >= 0 &&
          t[i + p[i] + 1] == t[i - p[i] - 1]
      p[i] += 1
    end
    if i + p[i] > r
      c = i
      r = i + p[i]
    end
  end
  p.max
end

raise "manacher wrong" unless manacher("abba") == 4
raise "manacher odd wrong" unless manacher("racecar") == 7
puts "[Ruby Manacher] Longest palindromic substring verified"
