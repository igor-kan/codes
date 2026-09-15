"""Egg dropping: minimum trials with k eggs and n floors."""
def egg_drop(eggs: int, floors: int) -> int:
    dp = [[0] * (eggs + 1) for _ in range(floors + 1)]
    trials = 0
    while dp[trials][eggs] < floors:
        trials += 1
        for k in range(1, eggs + 1):
            dp[trials][k] = dp[trials - 1][k - 1] + dp[trials - 1][k] + 1
    return trials


if __name__ == "__main__":
    assert egg_drop(2, 100) == 14
    assert egg_drop(1, 10) == 10
    print("egg drop ok")
