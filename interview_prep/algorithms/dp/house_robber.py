def rob(nums: list[int]) -> int:
    prev = cur = 0
    for n in nums:
        prev, cur = cur, max(cur, prev + n)
    return cur


if __name__ == "__main__":
    assert rob([2, 7, 9, 3, 1]) == 12
    print("ok")
