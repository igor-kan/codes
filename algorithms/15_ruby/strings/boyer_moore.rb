# Boyer-Moore-Horspool substring search.
def boyer_moore(text, pattern)
  n = text.length
  m = pattern.length
  skip = Array.new(256, m)
  (0...(m - 1)).each { |i| skip[pattern.getbyte(i)] = m - 1 - i }
  i = 0
  while i + m <= n
    j = m - 1
    j -= 1 while j >= 0 && text.getbyte(i + j) == pattern.getbyte(j)
    return i if j.negative?

    i += skip[text.getbyte(i + m - 1)]
  end
  -1
end

raise "search failed" unless boyer_moore("here is a simple example", "example") == 17
raise "search failed" unless boyer_moore("abc", "xyz") == -1

puts "boyer-moore ok"
