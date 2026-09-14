two_sum_sorted <- function(arr, target) {
  left <- 1
  right <- length(arr)
  while (left < right) {
    s <- arr[left] + arr[right]
    if (s == target) return(TRUE)
    if (s < target) left <- left + 1 else right <- right - 1
  }
  return(FALSE)
}

# Example
a <- c(1, 2, 3, 4, 5, 6)
stopifnot(two_sum_sorted(a, 9))
stopifnot(!two_sum_sorted(a, 15))
print("[R two_pointers] ... verified")
