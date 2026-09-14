knapsack <- function(weights, values, capacity) {
  n <- length(weights)
  dp <- rep(0, capacity + 1)
  
  for (i in 1:n) {
    if (weights[i] <= capacity) {
      for (w in capacity:weights[i]) {
        dp[w + 1] <- max(dp[w + 1], dp[w - weights[i] + 1] + values[i])
      }
    }
  }
  return(dp[capacity + 1])
}
