max_sum_subarray <- function(arr, k) {
  if (k <= 0 || length(arr) < k) return(0)
  window_sum <- sum(arr[1:k])
  max_sum <- window_sum
  n <- length(arr)
  if (k < n) {
    for (i in (k + 1):n) {
      window_sum <- window_sum + arr[i] - arr[i - k]
      max_sum <- max(max_sum, window_sum)
    }
  }
  max_sum
}

# Example
a <- c(2, 1, 5, 1, 3, 2)
stopifnot(max_sum_subarray(a, 3) == 9)
print("[R sliding_window] ... verified")
