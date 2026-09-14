"""Permutations, combinations and Catalan numbers."""
import math


def permutations(n: int, r: int) -> int:
    return math.perm(n, r)


def combinations(n: int, r: int) -> int:
    return math.comb(n, r)


def catalan(n: int) -> int:
    return math.comb(2 * n, n) // (n + 1)


def derangements(n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 0
    return (n - 1) * (derangements(n - 1) + derangements(n - 2))


if __name__ == "__main__":
    assert combinations(5, 2) == 10
    assert permutations(5, 2) == 20
    assert catalan(4) == 14
    assert derangements(4) == 9
    print("combinatorics ok")
