dsu_create <- function(n) {
  env <- new.env(parent = emptyenv())
  env$parent <- seq_len(n)
  env$rank <- integer(n)
  env
}

dsu_find <- function(dsu, x) {
  if (dsu$parent[x] != x) {
    dsu$parent[x] <- dsu_find(dsu, dsu$parent[x])
  }
  dsu$parent[x]
}

dsu_union <- function(dsu, x, y) {
  rx <- dsu_find(dsu, x)
  ry <- dsu_find(dsu, y)
  if (rx == ry) return(dsu)
  if (dsu$rank[rx] < dsu$rank[ry]) {
    tmp <- rx
    rx <- ry
    ry <- tmp
  }
  dsu$parent[ry] <- rx
  if (dsu$rank[rx] == dsu$rank[ry]) {
    dsu$rank[rx] <- dsu$rank[rx] + 1
  }
  dsu
}

dsu_connected <- function(dsu, x, y) {
  dsu_find(dsu, x) == dsu_find(dsu, y)
}

# Example
dsu <- dsu_create(5)
dsu <- dsu_union(dsu, 1, 2)
dsu <- dsu_union(dsu, 2, 3)
dsu <- dsu_union(dsu, 4, 5)
stopifnot(dsu_connected(dsu, 1, 3))
stopifnot(dsu_connected(dsu, 4, 5))
stopifnot(!dsu_connected(dsu, 1, 4))
print("[R dsu] ... verified")
