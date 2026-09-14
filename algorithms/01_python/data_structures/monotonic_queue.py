"""Monotonic deque: sliding window maximum in O(n)."""

from collections import deque
from typing import List


def sliding_window_max(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    if n == 0 or k == 0:
        return []
    dq = deque()
    res = []
    for i in range(n):
        if dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res


if __name__ == "__main__":
    assert sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert sliding_window_max([9, 8, 7, 6, 5], 2) == [9, 8, 7, 6]
    assert sliding_window_max([1, 2, 3], 1) == [1, 2, 3]
    print("[Python MonotonicQueue] Sliding window maximum verified.")
