dfs <- function(adj_list, start_node) {
  visited <- c()
  stack <- c(start_node)
  order <- c()
  
  while (length(stack) > 0) {
    node <- stack[length(stack)]
    stack <- stack[-length(stack)]
    
    if (!(node %in% visited)) {
      visited <- c(visited, node)
      order <- c(order, node)
      neighbors <- rev(adj_list[[as.character(node)]])
      stack <- c(stack, neighbors)
    }
  }
  return(order)
}
