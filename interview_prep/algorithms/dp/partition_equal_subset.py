def can_partition(nums: list[int]) -> bool:
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for n in nums:
        for value in range(target, n - 1, -1):
            dp[value] = dp[value] or dp[value - n]
    return dp[target]


if __name__ == "__main__":
    assert can_partition([1, 5, 11, 5])
    assert not can_partition([1, 2, 3, 5])
    print("ok")
