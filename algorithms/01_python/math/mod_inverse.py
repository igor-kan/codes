"""Modular inverse via extended Euclid and Fermat's little theorem (prime mod)."""


def extended_gcd(a: int, b: int):
    if b == 0:
        return a, 1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y


def mod_inverse_extended(a: int, m: int) -> int:
    """Modular inverse of a mod m; requires gcd(a, m) == 1."""
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError("Inverse does not exist")
    return x % m


def mod_inverse_fermat(a: int, p: int) -> int:
    """Modular inverse of a mod p where p is prime (a not divisible by p)."""
    if a % p == 0:
        raise ValueError("Inverse does not exist")
    return pow(a, p - 2, p)


if __name__ == "__main__":
    p = 1_000_000_007
    for a in [1, 2, 5, 123456, 987654321]:
        inv1 = mod_inverse_extended(a, p)
        inv2 = mod_inverse_fermat(a, p)
        assert inv1 == inv2
        assert (a * inv1) % p == 1
    print("[Python ModInverse] Extended Euclid and Fermat inverses verified.")
