"""Longest Increasing Subsequence in O(n log n) with reconstruction via patience sorting."""

from typing import List
from bisect import bisect_left


def length_of_lis(nums: List[int]) -> int:
    tails = []
    for x in nums:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


def lis_with_reconstruction(nums: List[int]) -> List[int]:
    """Returns one LIS as a list of values."""
    n = len(nums)
    if n == 0:
        return []
    tails = []
    tail_indices = []
    prev = [-1] * n
    for i, x in enumerate(nums):
        pos = bisect_left(tails, x)
        if pos == len(tails):
            tails.append(x)
            tail_indices.append(i)
        else:
            tails[pos] = x
            tail_indices[pos] = i
        if pos > 0:
            prev[i] = tail_indices[pos - 1]
    lis = []
    idx = tail_indices[-1]
    while idx != -1:
        lis.append(nums[idx])
        idx = prev[idx]
    return lis[::-1]


if __name__ == "__main__":
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    assert length_of_lis(arr) == 4
    assert length_of_lis([0, 1, 0, 3, 2, 3]) == 4
    assert length_of_lis([7, 7, 7, 7]) == 1
    seq = lis_with_reconstruction(arr)
    assert seq == [2, 3, 7, 18] or seq == [2, 5, 7, 101], seq
    print("[Python LIS] Longest increasing subsequence verified.")
