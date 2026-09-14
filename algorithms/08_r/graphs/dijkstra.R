dijkstra <- function(n, edges, start) {
  dist <- rep(Inf, n)
  dist[start] <- 0
  visited <- rep(FALSE, n)
  
  for (i in 1:(n - 1)) {
    unvisited_nodes <- which(!visited)
    if (length(unvisited_nodes) == 0) break
    u <- unvisited_nodes[which.min(dist[unvisited_nodes])]
    if (is.infinite(dist[u])) break
    visited[u] <- TRUE
    
    curr_edges <- edges[edges$from == u, ]
    if (nrow(curr_edges) > 0) {
      for (k in 1:nrow(curr_edges)) {
        v <- curr_edges$to[k]
        w <- curr_edges$weight[k]
        if (!visited[v] && dist[u] + w < dist[v]) {
          dist[v] <- dist[u] + w
        }
      }
    }
  }
  return(dist)
}
