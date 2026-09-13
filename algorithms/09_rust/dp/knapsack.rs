pub fn knapsack(weights:&[usize],values:&[i64],cap:usize)->i64{
    let mut dp=vec![0i64;cap+1];
    for i in 0..weights.len(){ for w in (weights[i]..=cap).rev(){
        dp[w]=dp[w].max(dp[w-weights[i]]+values[i]); } }
    dp[cap]
}