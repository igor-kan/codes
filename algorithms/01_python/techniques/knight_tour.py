"""Knight's tour using Warnsdorff's heuristic."""
MOVES = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]


def tour(n: int, start=(0, 0)) -> list[list[int]]:
    board = [[-1] * n for _ in range(n)]
    board[start[0]][start[1]] = 0

    def degree(r: int, c: int) -> int:
        return sum(
            0 <= r + dr < n and 0 <= c + dc < n and board[r + dr][c + dc] == -1
            for dr, dc in MOVES
        )

    r, c = start
    for step in range(1, n * n):
        candidates = [
            (degree(r + dr, c + dc), r + dr, c + dc)
            for dr, dc in MOVES
            if 0 <= r + dr < n and 0 <= c + dc < n and board[r + dr][c + dc] == -1
        ]
        if not candidates:
            return board
        _, r, c = min(candidates)
        board[r][c] = step
    return board


if __name__ == "__main__":
    board = tour(8)
    assert board[0][0] == 0
    values = [v for row in board for v in row]
    assert len(set(values)) == 64
    print("knight tour ok")
