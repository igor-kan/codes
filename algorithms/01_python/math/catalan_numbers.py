"""Catalan numbers via DP and the closed formula."""
import math


def catalan_dp(n: int) -> list[int]:
    catalan = [0] * (n + 1)
    catalan[0] = 1
    for i in range(1, n + 1):
        catalan[i] = sum(catalan[j] * catalan[i - 1 - j] for j in range(i))
    return catalan


def catalan(n: int) -> int:
    return math.comb(2 * n, n) // (n + 1)


if __name__ == "__main__":
    assert catalan_dp(5) == [1, 1, 2, 5, 14, 42]
    assert catalan(10) == 16796
    print("catalan numbers ok")
