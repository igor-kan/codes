"""nCr mod p via factorials + modular inverse, plus Pascal's triangle."""

from typing import List


class Combinatorics:
    def __init__(self, max_n: int, mod: int):
        self.mod = mod
        self.fact = [1] * (max_n + 1)
        self.inv_fact = [1] * (max_n + 1)
        for i in range(1, max_n + 1):
            self.fact[i] = self.fact[i - 1] * i % mod
        self.inv_fact[max_n] = pow(self.fact[max_n], mod - 2, mod)
        for i in range(max_n, 0, -1):
            self.inv_fact[i - 1] = self.inv_fact[i] * i % mod

    def ncr(self, n: int, r: int) -> int:
        if r < 0 or r > n:
            return 0
        return self.fact[n] * self.inv_fact[r] % self.mod * self.inv_fact[n - r] % self.mod


def pascals_triangle(n: int) -> List[List[int]]:
    """First n rows of Pascal's triangle (exact integers)."""
    rows = [[1]]
    for _ in range(1, n):
        prev = rows[-1]
        rows.append([1] + [prev[i] + prev[i + 1] for i in range(len(prev) - 1)] + [1])
    return rows


if __name__ == "__main__":
    MOD = 1_000_000_007
    comb = Combinatorics(100, MOD)
    assert comb.ncr(10, 3) == 120
    assert comb.ncr(10, 0) == 1
    assert comb.ncr(10, 10) == 1
    assert comb.ncr(10, 11) == 0

    tri = pascals_triangle(6)
    assert tri[4] == [1, 4, 6, 4, 1]
    assert tri[5] == [1, 5, 10, 10, 5, 1]
    # Verify row of Pascal matches nCr
    assert tri[5][2] == comb.ncr(5, 2)
    print("[Python nCr] Factorial inverse and Pascal's triangle verified.")
