bipartite_check <- function(n, edges) {
  graph <- vector("list", n)
  for (i in 1:n) graph[[i]] <- integer(0)
  for (k in seq_len(nrow(edges))) {
    u <- edges$from[k]
    v <- edges$to[k]
    graph[[u]] <- c(graph[[u]], v)
    graph[[v]] <- c(graph[[v]], u)
  }
  color <- rep(-1, n)
  for (start in 1:n) {
    if (color[start] != -1) next
    color[start] <- 0
    queue <- start
    while (length(queue) > 0) {
      u <- queue[1]
      queue <- queue[-1]
      for (v in graph[[u]]) {
        if (color[v] == -1) {
          color[v] <- 1 - color[u]
          queue <- c(queue, v)
        } else if (color[v] == color[u]) {
          return(FALSE)
        }
      }
    }
  }
  TRUE
}

# Example
even <- data.frame(from = c(1, 2, 3, 4), to = c(2, 3, 4, 1))
odd  <- data.frame(from = c(1, 2, 3), to = c(2, 3, 1))
stopifnot(bipartite_check(4, even))
stopifnot(!bipartite_check(3, odd))
print("[R bipartite_check] ... verified")
