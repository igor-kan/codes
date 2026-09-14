kahn_topological_sort <- function(n, edges) {
  graph <- vector("list", n)
  indegree <- integer(n)
  for (i in 1:n) graph[[i]] <- integer(0)
  for (k in seq_len(nrow(edges))) {
    u <- edges$from[k]
    v <- edges$to[k]
    graph[[u]] <- c(graph[[u]], v)
    indegree[v] <- indegree[v] + 1
  }
  queue <- which(indegree == 0)
  order <- integer(0)
  while (length(queue) > 0) {
    u <- queue[1]
    queue <- queue[-1]
    order <- c(order, u)
    for (v in graph[[u]]) {
      indegree[v] <- indegree[v] - 1
      if (indegree[v] == 0) queue <- c(queue, v)
    }
  }
  if (length(order) == n) order else integer(0)
}

# Example
edges <- data.frame(
  from = c(6, 6, 5, 5, 3, 4),
  to   = c(1, 3, 1, 2, 4, 2)
)
order <- kahn_topological_sort(6, edges)
stopifnot(length(order) == 6)
pos <- integer(6)
pos[order] <- seq_len(6)
stopifnot(all(pos[edges$from] < pos[edges$to]))
print("[R kahn_topological_sort] ... verified")
