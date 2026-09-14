def change(amount: int, coins: list[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for value in range(coin, amount + 1):
            dp[value] += dp[value - coin]
    return dp[amount]


if __name__ == "__main__":
    assert change(5, [1, 2, 5]) == 4
    print("ok")
