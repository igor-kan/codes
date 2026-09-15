"""2D Fenwick tree for rectangle sums."""
class Fenwick2D:
    def __init__(self, rows: int, cols: int) -> None:
        self.rows, self.cols = rows, cols
        self.tree = [[0] * (cols + 1) for _ in range(rows + 1)]

    def add(self, row: int, col: int, delta: int) -> None:
        i = row + 1
        while i <= self.rows:
            j = col + 1
            while j <= self.cols:
                self.tree[i][j] += delta
                j += j & -j
            i += i & -i

    def prefix(self, row: int, col: int) -> int:
        total = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                total += self.tree[i][j]
                j -= j & -j
            i -= i & -i
        return total

    def range_sum(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return (self.prefix(r2, c2) - self.prefix(r1 - 1, c2)
                - self.prefix(r2, c1 - 1) + self.prefix(r1 - 1, c1 - 1))


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    tree = Fenwick2D(3, 3)
    for r in range(3):
        for c in range(3):
            tree.add(r, c, matrix[r][c])
    assert tree.range_sum(0, 0, 2, 2) == 45
    assert tree.range_sum(1, 1, 2, 2) == 28
    print("fenwick 2d ok")
