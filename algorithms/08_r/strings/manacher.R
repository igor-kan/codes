manacher_odd <- function(s) {
  chars <- strsplit(s, "")[[1]]
  n <- length(chars)
  d <- rep(0, n)
  l <- 1
  r <- 0
  for (i in 1:n) {
    k <- if (i > r) 1 else min(d[l + r - i], r - i + 1)
    while (i - k >= 1 && i + k <= n && chars[i - k] == chars[i + k]) k <- k + 1
    d[i] <- k
    k <- k - 1
    if (i + k > r) {
      l <- i - k
      r <- i + k
    }
  }
  d
}

manacher_even <- function(s) {
  chars <- strsplit(s, "")[[1]]
  n <- length(chars)
  d <- rep(0, n)
  l <- 1
  r <- 0
  for (i in 1:n) {
    k <- if (i > r) 0 else min(d[l + r - i + 1], r - i + 1)
    while (i - k - 1 >= 1 && i + k <= n && chars[i - k - 1] == chars[i + k]) k <- k + 1
    d[i] <- k
    k <- k - 1
    if (i + k > r) {
      l <- i - k - 1
      r <- i + k
    }
  }
  d
}

longest_palindrome <- function(s) {
  if (nchar(s) == 0) return("")
  chars <- strsplit(s, "")[[1]]
  n <- length(chars)
  odd <- manacher_odd(s)
  even <- manacher_even(s)

  best_len <- 0
  best_start <- 1
  for (i in 1:n) {
    len <- 2 * odd[i] - 1
    if (len > best_len) {
      best_len <- len
      best_start <- i - odd[i] + 1
    }
    len <- 2 * even[i]
    if (len > best_len) {
      best_len <- len
      best_start <- i - even[i]
    }
  }
  paste0(chars[best_start:(best_start + best_len - 1)], collapse = "")
}

# Example
stopifnot(nchar(longest_palindrome("babad")) == 3)
stopifnot(nchar(longest_palindrome("abba")) == 4)
print("[R manacher] ... verified")
