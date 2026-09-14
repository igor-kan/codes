lower_bound <- function(arr, target) {
  lo <- 1
  hi <- length(arr) + 1
  while (lo < hi) {
    mid <- (lo + hi) %/% 2
    if (arr[mid] < target) lo <- mid + 1 else hi <- mid
  }
  lo
}

upper_bound <- function(arr, target) {
  lo <- 1
  hi <- length(arr) + 1
  while (lo < hi) {
    mid <- (lo + hi) %/% 2
    if (arr[mid] <= target) lo <- mid + 1 else hi <- mid
  }
  lo
}

# Example
a <- c(1, 2, 2, 2, 3, 5)
stopifnot(lower_bound(a, 2) == 2)
stopifnot(upper_bound(a, 2) == 5)
stopifnot(lower_bound(a, 4) == 6)
print("[R binary_search] ... verified")
