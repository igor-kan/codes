"""Two-pointer techniques: two-sum on sorted array and container with most water."""

from typing import List, Tuple, Optional


def two_sum_sorted(arr: List[int], target: int) -> Optional[Tuple[int, int]]:
    """Return indices (1-based) of two numbers summing to target, or None."""
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        s = arr[lo] + arr[hi]
        if s == target:
            return lo + 1, hi + 1
        elif s < target:
            lo += 1
        else:
            hi -= 1
    return None


def max_area(heights: List[int]) -> int:
    """Container with most water: maximum area between two lines."""
    lo, hi = 0, len(heights) - 1
    best = 0
    while lo < hi:
        area = min(heights[lo], heights[hi]) * (hi - lo)
        best = max(best, area)
        if heights[lo] < heights[hi]:
            lo += 1
        else:
            hi -= 1
    return best


if __name__ == "__main__":
    assert two_sum_sorted([2, 7, 11, 15], 9) == (1, 2)
    assert two_sum_sorted([1, 3, 4, 5], 8) == (2, 4)
    assert two_sum_sorted([1, 2], 5) is None

    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    print("[Python TwoPointers] two-sum and max-area verified.")
