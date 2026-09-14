"""List/dict/set comprehensions and generator expressions."""
import sys


def pythagorean(n: int) -> list[tuple[int, int, int]]:
    return [(a, b, c) for c in range(1, n)
            for a in range(1, c)
            for b in range(a, c)
            if a * a + b * b == c * c]


if __name__ == "__main__":
    assert pythagorean(20) == [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17)]
    squares = {n: n * n for n in range(5)}
    assert squares[4] == 16
    assert {n % 3 for n in range(10)} == {0, 1, 2}
    gen = (n * n for n in range(10_000))
    assert sys.getsizeof(gen) < sys.getsizeof([n * n for n in range(10_000)])
    print("ok")
