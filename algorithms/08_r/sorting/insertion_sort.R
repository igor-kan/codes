insertion_sort <- function(arr) {
  n <- length(arr)
  if (n <= 1) return(arr)
  for (i in 2:n) {
    key <- arr[i]
    j <- i - 1
    while (j >= 1 && arr[j] > key) {
      arr[j + 1] <- arr[j]
      j <- j - 1
    }
    arr[j + 1] <- key
  }
  arr
}

# Example
stopifnot(identical(insertion_sort(c(5, 2, 4, 6, 1, 3)), c(1, 2, 3, 4, 5, 6)))
print("[R insertion_sort] ... verified")
