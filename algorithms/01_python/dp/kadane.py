"""Kadane's algorithm for maximum subarray sum."""

from typing import List


def max_subarray_sum(nums: List[int]) -> int:
    best = nums[0]
    curr = nums[0]
    for x in nums[1:]:
        curr = max(x, curr + x)
        best = max(best, curr)
    return best


def max_subarray_with_indices(nums: List[int]):
    """Return (best_sum, start, end) inclusive indices."""
    best = nums[0]
    curr = nums[0]
    best_start = best_end = start = 0
    for i in range(1, len(nums)):
        if curr < 0:
            curr = nums[i]
            start = i
        else:
            curr += nums[i]
        if curr > best:
            best = curr
            best_start, best_end = start, i
    return best, best_start, best_end


if __name__ == "__main__":
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray_sum([5, 4, -1, 7, 8]) == 23
    assert max_subarray_sum([-1, -2, -3]) == -1
    total, s, e = max_subarray_with_indices([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    assert total == 6 and (s, e) == (3, 6)
    print("[Python Kadane] Maximum subarray sum verified.")
