# Catalan numbers by the recurrence.
catalan = Array.new(11, 0)
catalan[0] = 1
(1..10).each do |i|
  sum = 0
  (0...i).each { |j| sum += catalan[j] * catalan[i - 1 - j] }
  catalan[i] = sum
end
raise "wrong Catalan numbers" unless catalan[5] == 42 && catalan[10] == 16_796

puts "catalan(10)=#{catalan[10]}"
