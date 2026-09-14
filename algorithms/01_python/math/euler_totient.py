"""Euler's totient function phi(n): count of integers <= n coprime to n."""


def euler_phi(n: int) -> int:
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1 if p == 2 else 2
    if n > 1:
        result -= result // n
    return result


def euler_phi_1_to_n(n: int):
    """phi for all integers from 0 to n using a sieve."""
    phi = list(range(n + 1))
    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i
    return phi


if __name__ == "__main__":
    assert euler_phi(1) == 1
    assert euler_phi(9) == 6
    assert euler_phi(12) == 4
    assert euler_phi(36) == 12
    assert euler_phi(13) == 12

    phi = euler_phi_1_to_n(20)
    for i in range(1, 21):
        assert phi[i] == euler_phi(i), (i, phi[i], euler_phi(i))
    print("[Python EulerTotient] phi(n) verified.")
