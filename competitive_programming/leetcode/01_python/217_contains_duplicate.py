"""LeetCode 217 - Contains Duplicate."""
def contains_duplicate(nums):
    return len(nums) != len(set(nums))


if __name__ == "__main__":
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    print("217 contains duplicate ok")
