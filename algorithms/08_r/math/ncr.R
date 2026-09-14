mod_pow <- function(base, exp, mod) {
  result <- 1
  base <- base %% mod
  while (exp > 0) {
    if (exp %% 2 == 1) result <- (result * base) %% mod
    base <- (base * base) %% mod
    exp <- exp %/% 2
  }
  result
}

ncr <- function(n, r, mod) {
  if (r < 0 || r > n) return(0)
  fact <- rep(1, n + 1)
  inv_fact <- rep(1, n + 1)
  if (n >= 2) {
    for (i in 2:n) fact[i] <- (fact[i - 1] * i) %% mod
  }
  inv_fact[n + 1] <- mod_pow(fact[n + 1], mod - 2, mod)
  if (n >= 1) {
    for (i in n:1) inv_fact[i] <- (inv_fact[i + 1] * i) %% mod
  }
  fact[n + 1] * inv_fact[r + 1] %% mod * inv_fact[n - r + 1] %% mod
}

# Example
mod <- 1000000007
stopifnot(ncr(5, 2, mod) == 10)
stopifnot(ncr(10, 0, mod) == 1)
stopifnot(ncr(7, 7, mod) == 1)
print("[R ncr] ... verified")
