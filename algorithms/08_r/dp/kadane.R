kadane <- function(arr) {
  best <- arr[1]
  current <- arr[1]
  n <- length(arr)
  for (i in 2:n) {
    current <- max(arr[i], current + arr[i])
    best <- max(best, current)
  }
  best
}

# Example
a <- c(-2, 1, -3, 4, -1, 2, 1, -5, 4)
stopifnot(kadane(a) == 6)
print("[R kadane] ... verified")
