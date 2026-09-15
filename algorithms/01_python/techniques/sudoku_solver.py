"""Sudoku solver with backtracking."""
def solve(board: list[list[int]]) -> bool:
    def valid(row: int, col: int, value: int) -> bool:
        for i in range(9):
            if board[row][i] == value or board[i][col] == value:
                return False
        box_row, box_col = (row // 3) * 3, (col // 3) * 3
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if board[r][c] == value:
                    return False
        return True

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for value in range(1, 10):
                    if valid(row, col, value):
                        board[row][col] = value
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True


if __name__ == "__main__":
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    assert solve(puzzle)
    assert puzzle[0] == [5, 3, 4, 6, 7, 8, 9, 1, 2]
    print("sudoku solver ok")
