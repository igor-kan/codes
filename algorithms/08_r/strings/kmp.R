compute_lps <- function(pat) {
  p_chars <- strsplit(pat, "")[[1]]
  m <- length(p_chars)
  lps <- rep(0, m)
  len <- 0
  i <- 2
  while (i <= m) {
    if (p_chars[i] == p_chars[len + 1]) {
      len <- len + 1
      lps[i] <- len
      i <- i + 1
    } else if (len > 0) {
      len <- lps[len]
    } else {
      lps[i] <- 0
      i <- i + 1
    }
  }
  return(lps)
}

kmp_search <- function(text, pattern) {
  t_chars <- strsplit(text, "")[[1]]
  p_chars <- strsplit(pattern, "")[[1]]
  n <- length(t_chars)
  m <- length(p_chars)
  if (m == 0 || n < m) return(integer(0))
  
  lps <- compute_lps(pattern)
  matches <- c()
  i <- 1
  j <- 0
  
  while (i <= n) {
    if (t_chars[i] == p_chars[j + 1]) {
      i <- i + 1
      j <- j + 1
    }
    if (j == m) {
      matches <- c(matches, i - m)
      j <- lps[j]
    } else if (i <= n && t_chars[i] != p_chars[j + 1]) {
      if (j > 0) j <- lps[j] else i <- i + 1
    }
  }
  return(matches)
}
