"""Chinese Remainder Theorem for pairwise coprime moduli."""

from typing import List


def mod_inverse(a: int, m: int) -> int:
    a %= m
    g, x, _ = _extended_gcd(a, m)
    if g != 1:
        raise ValueError("Inverse does not exist")
    return x % m


def _extended_gcd(a: int, b: int):
    if b == 0:
        return a, 1, 0
    g, x, y = _extended_gcd(b, a % b)
    return g, y, x - (a // b) * y


def crt(remainders: List[int], moduli: List[int]) -> int:
    """Smallest non-negative x with x % moduli[i] == remainders[i] for all i.

    Moduli must be pairwise coprime.
    """
    x = 0
    M = 1
    for r, m in zip(remainders, moduli):
        M *= m
    for r, m in zip(remainders, moduli):
        Mi = M // m
        x += r * Mi * mod_inverse(Mi, m)
        x %= M
    return x % M


if __name__ == "__main__":
    # x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7) -> x = 23
    x = crt([2, 3, 2], [3, 5, 7])
    assert x == 23, x
    for r, m in zip([2, 3, 2], [3, 5, 7]):
        assert x % m == r
    # x ≡ 1 (mod 2), x ≡ 2 (mod 3) -> x = 5
    y = crt([1, 2], [2, 3])
    assert y == 5, y
    print("[Python CRT] Chinese Remainder Theorem verified.")
