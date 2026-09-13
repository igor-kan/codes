pub fn lcs(a:&[u8],b:&[u8])->usize{
    let (m,n)=(a.len(),b.len()); let mut dp=vec![vec![0usize;n+1];m+1];
    for i in 1..=m{ for j in 1..=n{
        dp[i][j]=if a[i-1]==b[j-1]{dp[i-1][j-1]+1}else{dp[i-1][j].max(dp[i][j-1])}; } }
    dp[m][n]
}