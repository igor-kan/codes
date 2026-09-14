"""The slice protocol and multidimensional slicing."""


class Grid:
    def __init__(self, rows: list[list[int]]) -> None:
        self.rows = rows

    def __getitem__(self, key):
        if isinstance(key, tuple):
            row, col = key
            return self.rows[row][col]
        return self.rows[key]


if __name__ == "__main__":
    data = list(range(10))
    assert data[2:8:2] == [2, 4, 6]
    assert data[::-1][:3] == [9, 8, 7]

    grid = Grid([[1, 2, 3], [4, 5, 6]])
    assert grid[0] == [1, 2, 3]
    assert grid[0, 1:] == [2, 3]
    print("ok")
