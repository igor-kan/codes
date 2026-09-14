"""Sliding window: max sum subarray of size k and longest substring without repeats."""

from typing import List


def max_sum_subarray_size_k(arr: List[int], k: int) -> int:
    n = len(arr)
    if k > n:
        return 0
    curr = sum(arr[:k])
    best = curr
    for i in range(k, n):
        curr += arr[i] - arr[i - k]
        best = max(best, curr)
    return best


def longest_substring_without_repeat(s: str) -> int:
    seen = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    assert max_sum_subarray_size_k([2, 1, 5, 1, 3, 2], 3) == 9
    assert max_sum_subarray_size_k([1, 2, 3, 4, 5], 2) == 9
    assert longest_substring_without_repeat("abcabcbb") == 3
    assert longest_substring_without_repeat("bbbbb") == 1
    assert longest_substring_without_repeat("pwwkew") == 3
    print("[Python SlidingWindow] max-sum and longest-substring verified.")
