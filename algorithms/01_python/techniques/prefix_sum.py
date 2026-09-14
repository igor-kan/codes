"""Prefix sum arrays for O(1) range sum queries in 1D and 2D."""

from typing import List


class PrefixSum1D:
    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.prefix = [0] * (self.n + 1)
        for i, v in enumerate(arr):
            self.prefix[i + 1] = self.prefix[i] + v

    def range_sum(self, l: int, r: int) -> int:
        """Sum of arr[l..r] inclusive."""
        return self.prefix[r + 1] - self.prefix[l]


class PrefixSum2D:
    def __init__(self, matrix: List[List[int]]):
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if matrix else 0
        self.prefix = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]
        for i in range(self.rows):
            for j in range(self.cols):
                self.prefix[i + 1][j + 1] = (
                    matrix[i][j]
                    + self.prefix[i][j + 1]
                    + self.prefix[i + 1][j]
                    - self.prefix[i][j]
                )

    def range_sum(self, r1: int, c1: int, r2: int, c2: int) -> int:
        """Sum of submatrix with top-left (r1,c1) and bottom-right (r2,c2)."""
        return (
            self.prefix[r2 + 1][c2 + 1]
            - self.prefix[r1][c2 + 1]
            - self.prefix[r2 + 1][c1]
            + self.prefix[r1][c1]
        )


if __name__ == "__main__":
    p1 = PrefixSum1D([1, 2, 3, 4, 5])
    assert p1.range_sum(0, 4) == 15
    assert p1.range_sum(1, 3) == 9
    assert p1.range_sum(2, 2) == 3

    p2 = PrefixSum2D([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert p2.range_sum(0, 0, 2, 2) == 45
    assert p2.range_sum(0, 0, 1, 1) == 12
    assert p2.range_sum(1, 1, 2, 2) == 28
    assert p2.range_sum(1, 1, 1, 1) == 5
    print("[Python PrefixSum] 1D and 2D range sums verified.")
