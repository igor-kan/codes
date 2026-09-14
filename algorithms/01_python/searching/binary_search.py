"""Binary search variants: lower_bound, upper_bound, and binary search on answer."""

from typing import List, Callable


def lower_bound(arr: List[int], target: int) -> int:
    """First index where arr[index] >= target."""
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def upper_bound(arr: List[int], target: int) -> int:
    """First index where arr[index] > target."""
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def binary_search(arr: List[int], target: int) -> int:
    """Exact index of target, or -1 if not present."""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def binary_search_answer(lo: int, hi: int, ok: Callable[[int], bool]) -> int:
    """Find smallest x in [lo, hi] where ok(x) is True (ok monotonic)."""
    while lo < hi:
        mid = (lo + hi) // 2
        if ok(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


if __name__ == "__main__":
    arr = [1, 2, 2, 2, 4, 5, 6]
    assert lower_bound(arr, 2) == 1
    assert lower_bound(arr, 3) == 4
    assert lower_bound(arr, 7) == 7
    assert upper_bound(arr, 2) == 4
    assert upper_bound(arr, 6) == 7
    assert binary_search(arr, 4) == 4
    assert binary_search(arr, 3) == -1

    # Smallest x with x*x >= 20
    x = binary_search_answer(0, 20, lambda m: m * m >= 20)
    assert x == 5
    print("[Python BinarySearch] lower_bound/upper_bound/answer verified.")
