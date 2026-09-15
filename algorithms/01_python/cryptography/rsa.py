"""RSA key generation, encryption and signing (toy key sizes)."""
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


def generate_keypair(bits: int = 32, seed: int = 0):
    rng = random.Random(seed)
    while True:
        p = rng.getrandbits(bits) | 1
        if is_prime(p):
            break
    while True:
        q = rng.getrandbits(bits) | 1
        if q != p and is_prime(q):
            break
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = pow(e, -1, phi)
    return (e, n), (d, n)


def encrypt(message: int, public: tuple[int, int]) -> int:
    e, n = public
    return pow(message, e, n)


def decrypt(ciphertext: int, private: tuple[int, int]) -> int:
    d, n = private
    return pow(ciphertext, d, n)


def sign(message: int, private: tuple[int, int]) -> int:
    d, n = private
    return pow(message, d, n)


def verify(signature: int, message: int, public: tuple[int, int]) -> bool:
    return encrypt(signature, public) == message % public[1]


if __name__ == "__main__":
    public, private = generate_keypair(seed=1)
    assert decrypt(encrypt(42, public), private) == 42
    assert verify(sign(7, private), 7, public)
    print("rsa ok")
