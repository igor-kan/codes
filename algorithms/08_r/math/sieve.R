sieve <- function(n) {
  if (n < 2) return(integer(0))
  is_prime <- rep(TRUE, n)
  is_prime[1] <- FALSE
  for (p in 2:floor(sqrt(n))) {
    if (is_prime[p]) {
      is_prime[seq(p * p, n, by = p)] <- FALSE
    }
  }
  return(which(is_prime))
}
