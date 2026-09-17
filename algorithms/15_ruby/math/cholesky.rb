# Cholesky LL^T in Ruby (Numerical Recipes 3rd Ed. Chapter 2.6)

def cholesky(a)
  n = a.size
  l = Array.new(n) { Array.new(n, 0.0) }

  n.times do |i|
    (0..i).each do |j|
      sum = (0...j).sum { |k| l[i][k] * l[j][k] }
      if i == j
        val = a[i][i] - sum
        raise "Not positive definite" if val <= 0
        l[i][j] = Math.sqrt(val)
      else
        l[i][j] = (a[i][j] - sum) / l[j][j]
      end
    end
  end
  l
end

a = [
  [4.0, 12.0, -16.0],
  [12.0, 37.0, -43.0],
  [-16.0, -43.0, 98.0]
]
l = cholesky(a)
raise "Failed" if (l[0][0] - 2.0).abs > 1e-6
puts "Ruby Cholesky verified."
