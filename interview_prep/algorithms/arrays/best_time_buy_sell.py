def max_profit(prices: list[int]) -> int:
    best = 0
    low = float("inf")
    for price in prices:
        low = min(low, price)
        best = max(best, price - low)
    return best


if __name__ == "__main__":
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    print("ok")
