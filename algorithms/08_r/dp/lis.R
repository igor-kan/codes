lower_bound_tails <- function(v, x) {
  lo <- 1
  hi <- length(v) + 1
  while (lo < hi) {
    mid <- (lo + hi) %/% 2
    if (v[mid] < x) lo <- mid + 1 else hi <- mid
  }
  lo
}

lis_length <- function(arr) {
  tails <- numeric(0)
  for (x in arr) {
    idx <- lower_bound_tails(tails, x)
    if (idx > length(tails)) {
      tails <- c(tails, x)
    } else {
      tails[idx] <- x
    }
  }
  length(tails)
}

# Example
a <- c(10, 9, 2, 5, 3, 7, 101, 18)
stopifnot(lis_length(a) == 4)
print("[R lis] ... verified")
