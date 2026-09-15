"""Extended Euclidean algorithm and modular inverse."""
def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    return gcd, y1, x1 - (a // b) * y1


def mod_inverse(a: int, modulus: int) -> int:
    gcd, x, _ = extended_gcd(a % modulus, modulus)
    if gcd != 1:
        raise ValueError("inverse does not exist")
    return x % modulus


def diophantine(a: int, b: int, c: int) -> tuple[int, int] | None:
    gcd, x, y = extended_gcd(a, b)
    if c % gcd:
        return None
    scale = c // gcd
    return x * scale, y * scale


if __name__ == "__main__":
    assert extended_gcd(30, 18)[0] == 6
    assert mod_inverse(3, 11) == 4
    assert diophantine(3, 6, 9) == (3, 0)
    print("extended gcd ok")
