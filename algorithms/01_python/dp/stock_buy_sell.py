"""Stock trading: one transaction and unlimited transactions."""
def max_profit_one(prices: list[int]) -> int:
    best, low = 0, float("inf")
    for price in prices:
        low = min(low, price)
        best = max(best, price - low)
    return best


def max_profit_unlimited(prices: list[int]) -> int:
    return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices)))


def max_profit_k(prices: list[int], k: int) -> int:
    if not prices:
        return 0
    buy = [-prices[0]] * (k + 1)
    sell = [0] * (k + 1)
    for price in prices[1:]:
        for t in range(1, k + 1):
            buy[t] = max(buy[t], sell[t - 1] - price)
            sell[t] = max(sell[t], buy[t] + price)
    return sell[k]


if __name__ == "__main__":
    assert max_profit_one([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit_unlimited([7, 1, 5, 3, 6, 4]) == 7
    assert max_profit_k([3, 2, 6, 5, 0, 3], 2) == 7
    print("stock dp ok")
