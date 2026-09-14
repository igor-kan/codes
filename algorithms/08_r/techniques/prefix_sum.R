prefix_sum <- function(arr) {
  c(0, cumsum(arr))
}

range_sum <- function(prefix, left, right) {
  prefix[right + 1] - prefix[left]
}

# Example
p <- prefix_sum(c(3, 1, 4, 1, 5, 9))
stopifnot(range_sum(p, 1, 3) == 8)
stopifnot(range_sum(p, 3, 5) == 10)
stopifnot(range_sum(p, 2, 4) == 6)
print("[R prefix_sum] ... verified")
