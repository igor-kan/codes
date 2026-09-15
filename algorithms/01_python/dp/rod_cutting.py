"""Rod cutting (CLRS 15.1)."""
from functools import lru_cache


def cut_rod(prices: list[int], n: int) -> int:
    best = [0] * (n + 1)
    for length in range(1, n + 1):
        best[length] = max(
            prices[i - 1] + best[length - i] for i in range(1, length + 1)
        )
    return best[n]


if __name__ == "__main__":
    prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    assert cut_rod(prices, 4) == 10
    assert cut_rod(prices, 7) == 18
    assert cut_rod(prices, 10) == 30
    print("rod cutting ok")
