def lcs(a, b)
  m, n = a.length, b.length
  dp = Array.new(m+1) { Array.new(n+1, 0) }
  (1..m).each { |i| (1..n).each { |j|
    dp[i][j] = a[i-1]==b[j-1] ? dp[i-1][j-1]+1 : [dp[i-1][j],dp[i][j-1]].max } }
  dp[m][n]
end