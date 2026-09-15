"""Digit DP: count numbers <= n with a digit-sum constraint."""
from functools import lru_cache


def count_with_digit_sum(n: int, target: int) -> int:
    digits = list(map(int, str(n)))

    @lru_cache(maxsize=None)
    def dp(pos: int, remaining: int, tight: bool) -> int:
        if remaining < 0:
            return 0
        if pos == len(digits):
            return 1 if remaining == 0 else 0
        limit = digits[pos] if tight else 9
        total = 0
        for d in range(limit + 1):
            total += dp(pos + 1, remaining - d, tight and d == limit)
        return total

    return dp(0, target, True)


if __name__ == "__main__":
    # Numbers <= 20 whose digits sum to 2: 2, 11, 20 -> 3
    assert count_with_digit_sum(20, 2) == 3
    print("digit dp ok")
