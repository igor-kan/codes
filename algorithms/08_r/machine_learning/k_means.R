kmeans_custom <- function(data, k, max_iters = 100) {
  data <- as.matrix(data)
  n <- nrow(data)
  centroids <- data[sample(1:n, k), , drop=FALSE]
  clusters <- rep(0, n)
  
  for (iter in 1:max_iters) {
    for (i in 1:n) {
      dists <- apply(centroids, 1, function(c) sum((data[i, ] - c)^2))
      clusters[i] <- which.min(dists)
    }
    
    new_centroids <- matrix(0, nrow = k, ncol = ncol(data))
    for (j in 1:k) {
      cluster_points <- data[clusters == j, , drop=FALSE]
      if (nrow(cluster_points) > 0) {
        new_centroids[j, ] <- colMeans(cluster_points)
      } else {
        new_centroids[j, ] <- data[sample(1:n, 1), ]
      }
    }
    
    if (all(centroids == new_centroids)) break
    centroids <- new_centroids
  }
  
  return(list(centroids = centroids, clusters = clusters))
}
