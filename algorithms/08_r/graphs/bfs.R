bfs <- function(adj_list, start_node) {
  visited <- c()
  queue <- c(start_node)
  order <- c()
  
  while (length(queue) > 0) {
    node <- queue[1]
    queue <- queue[-1]
    
    if (!(node %in% visited)) {
      visited <- c(visited, node)
      order <- c(order, node)
      neighbors <- adj_list[[as.character(node)]]
      queue <- c(queue, neighbors)
    }
  }
  return(order)
}
