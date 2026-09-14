gcd <- function(a, b) {
  while (b != 0) {
    temp <- b
    b <- a %% b
    a <- temp
  }
  return(a)
}

lcm <- function(a, b) {
  return(abs(a * b) / gcd(a, b))
}
