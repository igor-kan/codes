# ==============================================================================
# File: languages/08_r/pca_decomposition.R
# Language: R (Statistical Computing & Data Science)
# Domain: Multivariate Statistics & Dimensionality Reduction
# Algorithm: Principal Component Analysis (PCA) via Singular Value Decomposition (SVD)
#
# Rationale & Language Fit:
#   R was created by Ross Ihaka and Robert Gentleman as a modern dialect of S.
#   It represents the academic and industry gold standard for statistical computing,
#   bioinformatics, and econometrics. R treats matrices, data frames, and statistical
#   distributions as first-class citizens. Implementing PCA via SVD demonstrates R's
#   idiomatic matrix operations, numerical stability, vectorization, and rich S3
#   method formatting.
# ==============================================================================

#' Perform Principal Component Analysis via Singular Value Decomposition
#'
#' @param X A numeric matrix or data frame of observations (n rows) by variables (p columns).
#' @param center Logical, whether to mean-center the columns (default: TRUE).
#' @param scale. Logical, whether to scale columns to unit variance (default: TRUE).
#' @return A list of class 'svd_pca' containing:
#'   - center: column means used for centering
#'   - scale: column standard deviations used for scaling
#'   - loadings: matrix of eigenvectors / principal directions (p x p)
#'   - scores: coordinates of observations in PC space (n x p)
#'   - sdev: standard deviations of principal components (singular values / sqrt(n - 1))
#'   - var_explained: fraction of total variance explained by each PC
#'   - cum_var_explained: cumulative fraction of variance explained
svd_pca <- function(X, center = TRUE, scale. = TRUE) {
  X_mat <- as.matrix(X)
  n <- nrow(X_mat)
  p <- ncol(X_mat)
  
  if (n < 2) {
    stop("PCA requires at least 2 observations.")
  }
  
  # Step 1: Center and scale the data matrix
  col_means <- if (center) colMeans(X_mat) else rep(0, p)
  X_centered <- sweep(X_mat, 2, col_means, "-")
  
  col_sds <- if (scale.) {
    apply(X_centered, 2, sd)
  } else {
    rep(1, p)
  }
  
  # Guard against zero-variance variables
  col_sds[col_sds == 0] <- 1
  X_scaled <- sweep(X_centered, 2, col_sds, "/")
  
  # Step 2: Singular Value Decomposition (X = U * D * V^T)
  # For standardized X: Cov(X) = (1/(n-1)) * X^T * X = (1/(n-1)) * V * D^2 * V^T
  # Hence right singular vectors V are the principal component loadings.
  decomp <- svd(X_scaled)
  
  # Singular values to standard deviations of components
  singular_values <- decomp$d
  sdev <- singular_values / sqrt(n - 1)
  
  loadings <- decomp$v
  rownames(loadings) <- colnames(X_mat)
  colnames(loadings) <- paste0("PC", seq_len(min(n, p)))
  
  # Project data onto principal axes (scores = X * V)
  scores <- X_scaled %*% loadings
  rownames(scores) <- rownames(X_mat)
  colnames(scores) <- colnames(loadings)
  
  # Variance metrics
  eigenvalues <- sdev^2
  total_variance <- sum(eigenvalues)
  var_explained <- eigenvalues / total_variance
  cum_var <- cumsum(var_explained)
  
  result <- list(
    center = col_means,
    scale = col_sds,
    loadings = loadings,
    scores = scores,
    sdev = sdev,
    eigenvalues = eigenvalues,
    var_explained = var_explained,
    cum_var_explained = cum_var,
    n_obs = n,
    n_vars = p
  )
  class(result) <- "svd_pca"
  return(result)
}

#' Pretty-print method for svd_pca objects
print.svd_pca <- function(x, ...) {
  cat("=================================================================\n")
  cat("Principal Component Analysis via SVD (Custom R Engine)\n")
  cat(sprintf("Observations: %d | Variables: %d\n", x$n_obs, x$n_vars))
  cat("=================================================================\n\n")
  
  summary_tbl <- data.frame(
    `Std Deviation` = round(x$sdev, 4),
    `Eigenvalue` = round(x$eigenvalues, 4),
    `Proportion Var` = sprintf("%.2f%%", x$var_explained * 100),
    `Cumulative Var` = sprintf("%.2f%%", x$cum_var_explained * 100)
  )
  rownames(summary_tbl) <- colnames(x$loadings)
  print(summary_tbl)
  
  cat("\nFirst 3 Loadings (Eigenvectors):\n")
  k <- min(3, ncol(x$loadings))
  print(round(x$loadings[, 1:k, drop = FALSE], 4))
}

#' Text-based ASCII Scree Plot
scree_ascii_plot <- function(pca_obj) {
  cat("\n--- Scree Plot (Variance Explained per PC) ---\n")
  for (i in seq_along(pca_obj$var_explained)) {
    pct <- pca_obj$var_explained[i] * 100
    bar_len <- round(pct / 2)
    bar <- paste(rep("#", bar_len), collapse = "")
    cat(sprintf("PC%2d | %5.1f%% | %s\n", i, pct, bar))
  }
  cat("----------------------------------------------\n")
}

# --- Demonstration & Smoke Test ---
if (sys.nframe() == 0) {
  set.seed(42)
  cat("[R PCA Demo] Generating synthetic correlated multivariate dataset (N=150, P=5)...\n")
  
  # Latent factors
  z1 <- rnorm(150, mean = 0, sd = 3)
  z2 <- rnorm(150, mean = 0, sd = 1.5)
  
  # 5 observable variables with strong covariance
  x1 <- 0.9 * z1 + 0.2 * z2 + rnorm(150, sd = 0.5)
  x2 <- 0.8 * z1 - 0.4 * z2 + rnorm(150, sd = 0.5)
  x3 <- -0.7 * z1 + 0.5 * z2 + rnorm(150, sd = 0.5)
  x4 <- 0.1 * z1 + 0.9 * z2 + rnorm(150, sd = 0.5)
  x5 <- -0.2 * z1 - 0.8 * z2 + rnorm(150, sd = 0.5)
  
  df <- data.frame(Feature1 = x1, Feature2 = x2, Feature3 = x3, Feature4 = x4, Feature5 = x5)
  
  pca_res <- svd_pca(df, center = TRUE, scale. = TRUE)
  print(pca_res)
  scree_ascii_plot(pca_res)
  
  # Compare with base R prcomp to verify exact mathematical equivalence
  base_res <- prcomp(df, center = TRUE, scale. = TRUE)
  diff_sdev <- max(abs(pca_res$sdev - base_res$sdev))
  cat(sprintf("\nVerification vs. Base R prcomp(): Max absolute sdev difference = %.2e\n", diff_sdev))
  stopifnot(diff_sdev < 1e-12)
  cat("[SUCCESS] PCA implementation verified within double-precision numerical tolerance.\n")
}
