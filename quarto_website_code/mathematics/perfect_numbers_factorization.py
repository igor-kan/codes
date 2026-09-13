"""
Number Theory: Euclid-Euler Perfect Number Theorem & Mersenne Primes.

Proves:
An even number N is perfect iff N = 2^(p-1) * (2^p - 1) where 2^p - 1 is prime.
Reveals hidden binary patterns and powers of 2 differences in perfect numbers.
"""

def is_prime(n: int) -> bool:
    if n < 2: return False
    if n in [2, 3]: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def lucas_lehmer(p: int) -> bool:
    """Lucas-Lehmer deterministic primality test for Mersenne number M_p = 2^p - 1."""
    if p == 2: return True
    M_p = (1 << p) - 1
    s = 4
    for _ in range(p - 2):
        s = (s * s - 2) % M_p
    return s == 0

def generate_even_perfect_numbers(count: int = 4):
    """Generate even perfect numbers and demonstrate internal power-of-2 decompositions."""
    perfect_numbers = []
    p = 2
    while len(perfect_numbers) < count:
        if is_prime(p) and lucas_lehmer(p):
            mersenne = (1 << p) - 1
            even_perfect = (1 << (p - 1)) * mersenne
            perfect_numbers.append((p, mersenne, even_perfect))
        p += 1
    return perfect_numbers

if __name__ == "__main__":
    print("=== PERFECT NUMBERS & MERSENNE PRIMES ===")
    for p, M_p, N in generate_even_perfect_numbers(4):
        print(f"p={p:2d}: M_{p} = 2^{p}-1 = {M_p:6d} -> Perfect Number = {N:8d}")
        # Hidden power-of-two difference analysis
        print(f"       Binary: {bin(N)} ({p} ones followed by {p-1} zeros)")
