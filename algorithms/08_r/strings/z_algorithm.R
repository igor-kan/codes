z_algorithm <- function(s) {
  chars <- strsplit(s, "")[[1]]
  n <- length(chars)
  z <- rep(0, n)
  l <- 1
  r <- 0
  for (i in 2:n) {
    if (i <= r) z[i] <- min(r - i + 1, z[i - l + 1])
    while (i + z[i] <= n && chars[z[i] + 1] == chars[i + z[i]]) {
      z[i] <- z[i] + 1
    }
    if (i + z[i] - 1 > r) {
      l <- i
      r <- i + z[i] - 1
    }
  }
  z
}

# Example
z <- z_algorithm("ababab")
stopifnot(z[3] == 4)
stopifnot(z[5] == 2)
print("[R z_algorithm] ... verified")
