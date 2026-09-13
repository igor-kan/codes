func lcs(_ a: String, _ b: String) -> Int {
    let a=Array(a), b=Array(b), m=a.count, n=b.count
    var dp=Array(repeating:Array(repeating:0,count:n+1),count:m+1)
    for i in 1...m { for j in 1...n {
        dp[i][j]=a[i-1]==b[j-1] ? dp[i-1][j-1]+1 : max(dp[i-1][j],dp[i][j-1]) } }
    return dp[m][n]
}