"""LeetCode 283 - Move Zeroes."""
def move_zeroes(nums):
    result = [number for number in nums if number != 0]
    result.extend([0] * (len(nums) - len(result)))
    return result


if __name__ == "__main__":
    assert move_zeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert move_zeroes([0]) == [0]
    print("283 move zeroes ok")
