"""Minimum path sum in a grid."""
def min_path_sum(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    dp = [float("inf")] * cols
    dp[0] = 0
    for r in range(rows):
        dp[0] += grid[r][0]
        for c in range(1, cols):
            dp[c] = min(dp[c], dp[c - 1]) + grid[r][c]
    return dp[-1]


if __name__ == "__main__":
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    assert min_path_sum(grid) == 7
    print("min path sum ok")
