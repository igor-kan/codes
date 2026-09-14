"""Monotonic stack helpers: next greater element for a list."""

from typing import List


def next_greater(nums: List[int]) -> List[int]:
    """Returns index of next greater element for each position, or -1 if none."""
    n = len(nums)
    res = [-1] * n
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            res[stack.pop()] = i
        stack.append(i)
    return res


def prev_greater(nums: List[int]) -> List[int]:
    """Returns index of previous greater element for each position, or -1 if none."""
    n = len(nums)
    res = [-1] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and nums[stack[-1]] < nums[i]:
            res[stack.pop()] = i
        stack.append(i)
    return res


if __name__ == "__main__":
    nums = [2, 1, 4, 3, 5]
    nge = next_greater(nums)
    assert nge == [2, 2, 4, 4, -1], nge
    pge = prev_greater(nums)
    assert pge == [-1, 0, -1, 2, -1], pge
    print("[Python MonotonicStack] Next/previous greater element verified.")
