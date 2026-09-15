"""LeetCode 1480 - Running Sum of 1d Array."""
def running_sum(nums):
    result = []
    total = 0
    for value in nums:
        total += value
        result.append(total)
    return result


if __name__ == "__main__":
    assert running_sum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert running_sum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
    print("1480 running sum ok")
