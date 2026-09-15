"""Pollard's rho integer factorization with Miller-Rabin."""
import math
import random


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def pollard_rho(n: int) -> int:
    if n % 2 == 0:
        return 2
    while True:
        x = random.randrange(2, n)
        y, c, d = x, random.randrange(1, n), 1
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = math.gcd(abs(x - y), n)
        if d != n:
            return d


def factorize(n: int) -> list[int]:
    if n == 1:
        return []
    if is_prime(n):
        return [n]
    factor = pollard_rho(n)
    return sorted(factorize(factor) + factorize(n // factor))


if __name__ == "__main__":
    random.seed(0)
    assert factorize(2 * 3 * 5 * 7 * 11) == [2, 3, 5, 7, 11]
    assert is_prime(97) and not is_prime(100)
    print("pollard rho ok")
