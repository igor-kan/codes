"""Codeforces 263A - Beautiful Matrix."""
def beautiful_matrix(grid):
    for row in range(5):
        for column in range(5):
            if grid[row][column] == 1:
                return abs(row - 2) + abs(column - 2)
    return -1


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    assert beautiful_matrix(grid) == 3
    print("263A beautiful matrix ok")
