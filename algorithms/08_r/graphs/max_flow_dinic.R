max_flow_dinic <- function(n, edges, source, sink) {
  m <- nrow(edges)
  g <- new.env(parent = emptyenv())
  g$graph <- vector("list", n)
  for (i in 1:n) g$graph[[i]] <- integer(0)
  g$to <- integer(2 * m)
  g$cap <- numeric(2 * m)
  g$rev <- integer(2 * m)
  for (k in seq_len(m)) {
    u <- edges$from[k]
    v <- edges$to[k]
    c <- edges$capacity[k]
    fwd <- 2 * k - 1
    bwd <- 2 * k
    g$to[fwd] <- v
    g$cap[fwd] <- c
    g$rev[fwd] <- bwd
    g$to[bwd] <- u
    g$cap[bwd] <- 0
    g$rev[bwd] <- fwd
    g$graph[[u]] <- c(g$graph[[u]], fwd)
    g$graph[[v]] <- c(g$graph[[v]], bwd)
  }
  g$level <- integer(n)
  g$iter <- integer(n)

  bfs <- function() {
    g$level <- rep(-1, n)
    g$level[source] <- 0
    q <- source
    while (length(q) > 0) {
      u <- q[1]
      q <- q[-1]
      for (e in g$graph[[u]]) {
        if (g$cap[e] > 0 && g$level[g$to[e]] < 0) {
          g$level[g$to[e]] <- g$level[u] + 1
          q <- c(q, g$to[e])
        }
      }
    }
    g$level[sink] >= 0
  }

  dfs <- function(u, pushed) {
    if (u == sink) return(pushed)
    while (g$iter[u] < length(g$graph[[u]])) {
      g$iter[u] <- g$iter[u] + 1
      e <- g$graph[[u]][g$iter[u]]
      if (g$cap[e] > 0 && g$level[u] < g$level[g$to[e]]) {
        tr <- dfs(g$to[e], min(pushed, g$cap[e]))
        if (tr > 0) {
          g$cap[e] <- g$cap[e] - tr
          g$cap[g$rev[e]] <- g$cap[g$rev[e]] + tr
          return(tr)
        }
      }
    }
    return(0)
  }

  flow <- 0
  while (bfs()) {
    g$iter <- integer(n)
    repeat {
      f <- dfs(source, Inf)
      if (f == 0) break
      flow <- flow + f
    }
  }
  flow
}

# Example
edges <- data.frame(
  from     = c(1, 1, 2, 2, 2, 3, 4, 5, 5),
  to       = c(2, 3, 3, 4, 5, 5, 6, 4, 6),
  capacity = c(10, 10, 2, 4, 8, 9, 10, 6, 10)
)
stopifnot(max_flow_dinic(6, edges, 1, 6) == 19)
print("[R max_flow_dinic] ... verified")
