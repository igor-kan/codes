"""Burst balloons: maximize coins."""
def max_coins(nums: list[int]) -> int:
    values = [1, *nums, 1]
    n = len(values)
    dp = [[0] * n for _ in range(n)]
    for length in range(1, n - 1):
        for left in range(0, n - length - 1):
            right = left + length + 1
            for k in range(left + 1, right):
                coins = values[left] * values[k] * values[right]
                dp[left][right] = max(dp[left][right], coins + dp[left][k] + dp[k][right])
    return dp[0][n - 1]


if __name__ == "__main__":
    assert max_coins([3, 1, 5, 8]) == 167
    print("burst balloons ok")
