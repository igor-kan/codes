"""Count lattice paths with obstacles."""
def unique_paths_with_obstacles(grid: list[list[int]]) -> int:
    cols = len(grid[0])
    dp = [0] * cols
    dp[0] = 1
    for row in grid:
        for c in range(cols):
            if row[c] == 1:
                dp[c] = 0
            elif c > 0:
                dp[c] += dp[c - 1]
    return dp[-1]


if __name__ == "__main__":
    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert unique_paths_with_obstacles(grid) == 2
    print("unique paths ii ok")
