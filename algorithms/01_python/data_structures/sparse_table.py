"""Sparse Table for O(1) range minimum/maximum queries over an immutable array."""

from typing import List


class SparseTable:
    def __init__(self, data: List[int], mode: str = "min"):
        assert mode in ("min", "max")
        self.n = len(data)
        self.mode = mode
        self.log = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log[i] = self.log[i // 2] + 1

        k = self.log[self.n] + 1
        self.st = [data[:]]
        for j in range(1, k):
            prev = self.st[j - 1]
            step = 1 << (j - 1)
            if self.mode == "min":
                row = [min(prev[i], prev[i + step]) for i in range(self.n - (1 << j) + 1)]
            else:
                row = [max(prev[i], prev[i + step]) for i in range(self.n - (1 << j) + 1)]
            self.st.append(row)

    def _op(self, a, b):
        return min(a, b) if self.mode == "min" else max(a, b)

    def query(self, l: int, r: int) -> int:
        """Query over [l, r] inclusive."""
        j = self.log[r - l + 1]
        return self._op(self.st[j][l], self.st[j][r - (1 << j) + 1])


if __name__ == "__main__":
    arr = [4, 2, 7, 1, 8, 3, 6, 5]
    st_min = SparseTable(arr, "min")
    st_max = SparseTable(arr, "max")
    assert st_min.query(0, 7) == 1
    assert st_min.query(2, 4) == 1
    assert st_min.query(0, 1) == 2
    assert st_max.query(0, 7) == 8
    assert st_max.query(1, 3) == 7
    assert st_max.query(4, 4) == 8
    print("[Python SparseTable] Range min/max queries verified.")
