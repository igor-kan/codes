segment_tree_create <- function(values) {
  n <- length(values)
  size <- 1
  while (size < n) size <- size * 2
  tree <- rep(0, 2 * size)
  tree[size:(size + n - 1)] <- values
  for (i in (size - 1):1) {
    tree[i] <- tree[2 * i] + tree[2 * i + 1]
  }
  env <- new.env(parent = emptyenv())
  env$size <- size
  env$n <- n
  env$tree <- tree
  env
}

segment_tree_update <- function(st, pos, value) {
  size <- st$size
  tree <- st$tree
  idx <- pos + size - 1
  tree[idx] <- value
  idx <- idx %/% 2
  while (idx >= 1) {
    tree[idx] <- tree[2 * idx] + tree[2 * idx + 1]
    idx <- idx %/% 2
  }
  st$tree <- tree
  st
}

segment_tree_query <- function(st, l, r) {
  size <- st$size
  tree <- st$tree
  l <- l + size - 1
  r <- r + size - 1
  res <- 0
  while (l <= r) {
    if (l %% 2 == 1) {
      res <- res + tree[l]
      l <- l + 1
    }
    if (r %% 2 == 0) {
      res <- res + tree[r]
      r <- r - 1
    }
    l <- l %/% 2
    r <- r %/% 2
  }
  res
}

# Example
st <- segment_tree_create(c(1, 3, 5, 7, 9, 11))
st <- segment_tree_update(st, 3, 10)  # c(1, 3, 10, 7, 9, 11)
stopifnot(segment_tree_query(st, 1, 3) == 14)
stopifnot(segment_tree_query(st, 2, 5) == 29)
stopifnot(segment_tree_query(st, 1, 6) == 41)
print("[R segment_tree] ... verified")
