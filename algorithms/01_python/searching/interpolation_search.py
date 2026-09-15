"""Interpolation search for uniformly distributed sorted data."""
def interpolation_search(a: list, target: int) -> int:
    lo, hi = 0, len(a) - 1
    while lo <= hi and a[lo] <= target <= a[hi]:
        if a[hi] == a[lo]:
            return lo if a[lo] == target else -1
        pos = lo + (target - a[lo]) * (hi - lo) // (a[hi] - a[lo])
        if a[pos] == target:
            return pos
        if a[pos] < target:
            lo = pos + 1
        else:
            hi = pos - 1
    return -1


if __name__ == "__main__":
    arr = list(range(0, 100, 2))
    assert interpolation_search(arr, 42) == 21
    print("interpolation search ok")
