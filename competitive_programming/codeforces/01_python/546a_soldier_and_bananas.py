"""Codeforces 546A - Soldier and Bananas."""
def soldier_and_bananas(cost, money, count):
    total = cost * count * (count + 1) // 2
    return max(0, total - money)


if __name__ == "__main__":
    assert soldier_and_bananas(3, 17, 4) == 13
    assert soldier_and_bananas(1, 100, 1) == 0
    print("546A soldier and bananas ok")
