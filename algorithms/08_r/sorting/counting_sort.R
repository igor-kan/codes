counting_sort <- function(arr) {
  if (length(arr) == 0) return(arr)
  min_val <- min(arr)
  max_val <- max(arr)
  counts <- integer(max_val - min_val + 1)
  for (x in arr) {
    counts[x - min_val + 1] <- counts[x - min_val + 1] + 1
  }
  rep(min_val:max_val, times = counts)
}

# Example
sorted <- counting_sort(c(4, 2, 2, 8, 3, 3, 1))
stopifnot(identical(sorted, c(1, 2, 2, 3, 3, 4, 8)))
print("[R counting_sort] ... verified")
