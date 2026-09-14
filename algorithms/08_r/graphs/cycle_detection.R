cycle_detection <- function(n, edges) {
  graph <- vector("list", n)
  for (i in 1:n) graph[[i]] <- integer(0)
  for (k in seq_len(nrow(edges))) {
    u <- edges$from[k]
    v <- edges$to[k]
    graph[[u]] <- c(graph[[u]], v)
  }
  state <- integer(n)  # 0 unvisited, 1 visiting, 2 done

  dfs <- function(u) {
    state[u] <<- 1
    for (v in graph[[u]]) {
      if (state[v] == 1) return(TRUE)
      if (state[v] == 0 && dfs(v)) return(TRUE)
    }
    state[u] <<- 2
    FALSE
  }

  for (i in 1:n) {
    if (state[i] == 0 && dfs(i)) return(TRUE)
  }
  FALSE
}

# Example
with_cycle <- data.frame(from = c(1, 2, 3), to = c(2, 3, 1))
acyclic <- data.frame(from = c(1, 2, 1), to = c(2, 3, 3))
stopifnot(cycle_detection(3, with_cycle))
stopifnot(!cycle_detection(3, acyclic))
print("[R cycle_detection] ... verified")
