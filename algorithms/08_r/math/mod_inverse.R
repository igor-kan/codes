mod_gcd <- function(a, b) {
  while (b != 0) {
    temp <- b
    b <- a %% b
    a <- temp
  }
  a
}

extended_gcd <- function(a, b) {
  if (b == 0) return(c(1, 0))
  res <- extended_gcd(b, a %% b)
  c(res[2], res[1] - (a %/% b) * res[2])
}

mod_inverse <- function(a, mod) {
  a <- a %% mod
  if (mod_gcd(a, mod) != 1) return(NA)
  res <- extended_gcd(a, mod)
  ((res[1] %% mod) + mod) %% mod
}

# Example
mod <- 1000000007
inv3 <- mod_inverse(3, mod)
stopifnot((3 * inv3) %% mod == 1)
print("[R mod_inverse] ... verified")
