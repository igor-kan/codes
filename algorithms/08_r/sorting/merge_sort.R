merge_sort <- function(arr) {
  if (length(arr) <= 1) return(arr)
  mid <- length(arr) %/% 2
  left <- merge_sort(arr[1:mid])
  right <- merge_sort(arr[(mid + 1):length(arr)])
  
  res <- c()
  i <- 1
  j <- 1
  while (i <= length(left) && j <= length(right)) {
    if (left[i] <= right[j]) {
      res <- c(res, left[i])
      i <- i + 1
    } else {
      res <- c(res, right[j])
      j <- j + 1
    }
  }
  if (i <= length(left)) res <- c(res, left[i:length(left)])
  if (j <= length(right)) res <- c(res, right[j:length(right)])
  return(res)
}
