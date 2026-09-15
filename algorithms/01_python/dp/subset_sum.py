"""Subset-sum feasibility and count with DP."""
def subset_sum(nums: list[int], target: int) -> bool:
    reachable = [False] * (target + 1)
    reachable[0] = True
    for n in nums:
        for value in range(target, n - 1, -1):
            reachable[value] = reachable[value] or reachable[value - n]
    return reachable[target]


def count_subsets(nums: list[int], target: int) -> int:
    dp = [0] * (target + 1)
    dp[0] = 1
    for n in nums:
        for value in range(target, n - 1, -1):
            dp[value] += dp[value - n]
    return dp[target]


if __name__ == "__main__":
    assert subset_sum([3, 34, 4, 12, 5, 2], 9)
    assert not subset_sum([3, 34, 4, 12, 5, 2], 30)
    assert count_subsets([1, 2, 3, 3], 6) == 3
    print("subset sum ok")
