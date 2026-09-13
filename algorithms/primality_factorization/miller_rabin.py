import math
import random


def mod_pow(base: int, exp: int, mod: int) -> int:
    return pow(base, exp, mod)


def is_prime_mr(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for a in bases:
        if n <= a:
            break
        x = mod_pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def pollard_rho(n: int) -> int:
    if n % 2 == 0:
        return 2
    if is_prime_mr(n):
        return n

    x = random.randint(2, n - 1)
    y = x
    c = random.randint(1, n - 1)
    g = 1

    f = lambda v: (pow(v, 2, n) + c) % n

    while g == 1:
        x = f(x)
        y = f(f(y))
        g = math.gcd(abs(x - y), n)
        if g == n:
            return pollard_rho(n)
    return g


if __name__ == "__main__":
    p1 = 1000000007
    p2 = 2147483647
    composite = p1 * p2

    assert is_prime_mr(p1) is True
    assert is_prime_mr(p2) is True
    assert is_prime_mr(composite) is False

    factor = pollard_rho(composite)
    assert factor in (p1, p2)
    print(f"[Python Pollard's Rho] Factored {composite} -> {factor} * {composite // factor}")
