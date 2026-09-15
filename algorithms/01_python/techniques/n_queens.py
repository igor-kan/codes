"""N-queens: count and return one solution."""
def solve(n: int) -> list[list[str]] | None:
    columns: set[int] = set()
    diagonals: set[int] = set()
    anti: set[int] = set()
    board: list[int] = []

    def place(row: int) -> bool:
        if row == n:
            return True
        for col in range(n):
            if col in columns or (row - col) in diagonals or (row + col) in anti:
                continue
            columns.add(col)
            diagonals.add(row - col)
            anti.add(row + col)
            board.append(col)
            if place(row + 1):
                return True
            board.pop()
            columns.discard(col)
            diagonals.discard(row - col)
            anti.discard(row + col)
        return False

    if not place(0):
        return None
    return ["".join("Q" if c == col else "." for c in range(n)) for col in board]


def count(n: int) -> int:
    columns: set[int] = set()
    diagonals: set[int] = set()
    anti: set[int] = set()

    def place(row: int) -> int:
        if row == n:
            return 1
        total = 0
        for col in range(n):
            if col in columns or (row - col) in diagonals or (row + col) in anti:
                continue
            columns.add(col)
            diagonals.add(row - col)
            anti.add(row + col)
            total += place(row + 1)
            columns.discard(col)
            diagonals.discard(row - col)
            anti.discard(row + col)
        return total

    return place(0)


if __name__ == "__main__":
    assert count(8) == 92
    assert count(4) == 2
    assert solve(4) is not None
    print("n-queens ok")
