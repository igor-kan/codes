"""LeetCode 27 - Remove Element."""
def remove_element(nums, value):
    return [number for number in nums if number != value]


if __name__ == "__main__":
    assert remove_element([3, 2, 2, 3], 3) == [2, 2]
    assert remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2) == [0, 1, 3, 0, 4]
    print("27 remove element ok")
