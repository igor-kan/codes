"""Segmented sieve for primes in a range."""
def simple_sieve(limit: int) -> list[int]:
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i, prime in enumerate(sieve) if prime]


def segmented_sieve(low: int, high: int) -> list[int]:
    base_primes = simple_sieve(int(high ** 0.5) + 1)
    segment = [True] * (high - low + 1)
    for prime in base_primes:
        start = max(prime * prime, (low + prime - 1) // prime * prime)
        for value in range(start, high + 1, prime):
            segment[value - low] = False
    if low <= 1:
        segment[0] = False
    return [low + i for i, prime in enumerate(segment) if prime]


if __name__ == "__main__":
    assert segmented_sieve(10, 30) == [11, 13, 17, 19, 23, 29]
    print("segmented sieve ok")
