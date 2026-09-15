"""LeetCode 268 - Missing Number."""
def missing_number(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)


if __name__ == "__main__":
    assert missing_number([3, 0, 1]) == 2
    assert missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    print("268 missing number ok")
