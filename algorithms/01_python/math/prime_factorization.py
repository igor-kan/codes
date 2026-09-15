"""Trial-division prime factorization with a wheel."""
def factorize(n: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2
    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            n //= divisor
        divisor += 2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def divisors(n: int) -> list[int]:
    result = [1]
    for prime, exponent in factorize(n).items():
        result = [d * prime ** e for d in result for e in range(exponent + 1)]
    return sorted(result)


if __name__ == "__main__":
    assert factorize(360) == {2: 3, 3: 2, 5: 1}
    assert divisors(28) == [1, 2, 4, 7, 14, 28]
    print("prime factorization ok")
