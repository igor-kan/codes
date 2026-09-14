quick_sort <- function(arr) {
  if (length(arr) <= 1) return(arr)
  pivot <- arr[ceiling(length(arr) / 2)]
  left <- arr[arr < pivot]
  mid <- arr[arr == pivot]
  right <- arr[arr > pivot]
  return(c(quick_sort(left), mid, quick_sort(right)))
}
