"""Counting sort for non-negative integer arrays."""

from typing import List


def counting_sort(arr: List[int]) -> List[int]:
    if not arr:
        return []
    max_val = max(arr)
    counts = [0] * (max_val + 1)
    for x in arr:
        counts[x] += 1
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    result = [0] * len(arr)
    for x in reversed(arr):
        counts[x] -= 1
        result[counts[x]] = x
    return result


if __name__ == "__main__":
    assert counting_sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]
    assert counting_sort([5, 0, 5, 0, 5]) == [0, 0, 5, 5, 5]
    assert counting_sort([]) == []
    assert counting_sort([7]) == [7]
    print("[Python CountingSort] verified.")
