"""LeetCode 26 - Remove Duplicates from Sorted Array."""
def remove_duplicates(nums):
    result = []
    for value in nums:
        if not result or result[-1] != value:
            result.append(value)
    return result


if __name__ == "__main__":
    assert remove_duplicates([1, 1, 2]) == [1, 2]
    assert remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == [0, 1, 2, 3, 4]
    print("26 remove duplicates ok")
