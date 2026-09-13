function knapsack(weights, values, cap) {
  const dp = new Array(cap+1).fill(0);
  for (let i=0;i<weights.length;i++)
    for (let w=cap;w>=weights[i];w--)
      dp[w] = Math.max(dp[w], dp[w-weights[i]]+values[i]);
  return dp[cap];
}
module.exports = { knapsack };