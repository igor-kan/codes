"""Exponential search on a sorted array."""
def exponential_search(a: list, target: int) -> int:
    if not a:
        return -1
    if a[0] == target:
        return 0
    bound = 1
    while bound < len(a) and a[bound] < target:
        bound *= 2
    lo, hi = bound // 2, min(bound, len(a) - 1)
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == target:
            return mid
        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40, 55, 77, 101]
    assert exponential_search(arr, 10) == 3
    assert exponential_search(arr, 100) == -1
    print("exponential search ok")
