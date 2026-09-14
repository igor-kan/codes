"""Matrix Chain Multiplication in O(n^3)."""

from typing import List, Tuple


def matrix_chain_order(dims: List[int]) -> Tuple[int, List[List[int]]]:
    """Minimum scalar multiplications and the split table for reconstruction."""
    n = len(dims) - 1
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            m[i][j] = float("inf")
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k
    return m[0][n - 1], s


def _build_parens(s: List[List[int]], i: int, j: int) -> str:
    if i == j:
        return f"A{i}"
    k = s[i][j]
    return f"({_build_parens(s, i, k)} x {_build_parens(s, k + 1, j)})"


def parens(s: List[List[int]], n: int) -> str:
    return _build_parens(s, 0, n - 1)


if __name__ == "__main__":
    dims = [10, 20, 30, 40, 30]
    cost, s = matrix_chain_order(dims)
    assert cost == 30000, cost
    dims2 = [1, 2, 3, 4]
    cost2, s2 = matrix_chain_order(dims2)
    assert cost2 == 18, cost2
    print(f"[Python MatrixChain] Minimum multiplications = {cost}, {parens(s, len(dims) - 1)}")
