lca_binary_lifting <- function(n, edges, root = 1) {
  LOG <- ceiling(log2(n)) + 1
  graph <- vector("list", n)
  for (i in 1:n) graph[[i]] <- integer(0)
  for (k in seq_len(nrow(edges))) {
    u <- edges$from[k]
    v <- edges$to[k]
    graph[[u]] <- c(graph[[u]], v)
    graph[[v]] <- c(graph[[v]], u)
  }
  up <- matrix(0, nrow = n, ncol = LOG)
  depth <- integer(n)
  visited <- logical(n)

  dfs <- function(u, parent) {
    visited[u] <<- TRUE
    up[u, 1] <<- parent
    if (LOG > 1) {
      for (j in 2:LOG) {
        up[u, j] <<- up[up[u, j - 1], j - 1]
      }
    }
    for (v in graph[[u]]) {
      if (!visited[v]) {
        depth[v] <<- depth[u] + 1
        dfs(v, u)
      }
    }
  }

  dfs(root, root)

  query <- function(a, b) {
    if (depth[a] < depth[b]) {
      tmp <- a
      a <- b
      b <- tmp
    }
    diff <- depth[a] - depth[b]
    j <- 1
    while (diff > 0) {
      if (diff %% 2 == 1) a <- up[a, j]
      diff <- diff %/% 2
      j <- j + 1
    }
    if (a == b) return(a)
    for (j in LOG:1) {
      if (up[a, j] != up[b, j]) {
        a <- up[a, j]
        b <- up[b, j]
      }
    }
    up[a, 1]
  }

  list(query = query, depth = depth, up = up)
}

# Example
edges <- data.frame(from = c(1, 1, 2, 2, 3), to = c(2, 3, 4, 5, 6))
lca <- lca_binary_lifting(6, edges, root = 1)
stopifnot(lca$query(4, 5) == 2)
stopifnot(lca$query(4, 6) == 1)
stopifnot(lca$query(4, 2) == 2)
print("[R lca_binary_lifting] ... verified")
