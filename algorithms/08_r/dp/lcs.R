lcs <- function(s1, s2) {
  chars1 <- strsplit(s1, "")[[1]]
  chars2 <- strsplit(s2, "")[[1]]
  m <- length(chars1)
  n <- length(chars2)
  
  dp <- matrix(0, nrow = m + 1, ncol = n + 1)
  for (i in 1:m) {
    for (j in 1:n) {
      if (chars1[i] == chars2[j]) {
        dp[i + 1, j + 1] <- dp[i, j] + 1
      } else {
        dp[i + 1, j + 1] <- max(dp[i + 1, j], dp[i, j + 1])
      }
    }
  }
  return(dp[m + 1, n + 1])
}
