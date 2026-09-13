def gcd(a, b) = b == 0 ? a : gcd(b, a % b)
def lcm(a, b) = a / gcd(a, b) * b