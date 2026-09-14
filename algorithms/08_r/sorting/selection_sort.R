selection_sort <- function(arr) {
  n <- length(arr)
  if (n <= 1) return(arr)
  for (i in 1:(n - 1)) {
    min_idx <- i
    for (j in (i + 1):n) {
      if (arr[j] < arr[min_idx]) min_idx <- j
    }
    temp <- arr[i]
    arr[i] <- arr[min_idx]
    arr[min_idx] <- temp
  }
  arr
}

# Example
stopifnot(identical(selection_sort(c(64, 25, 12, 22, 11)), c(11, 12, 22, 25, 64)))
print("[R selection_sort] ... verified")
