"""Quickselect: expected linear-time order statistic (CLRS 9.2)."""
import random


def quickselect(values: list[int], k: int) -> int:
    if not 0 <= k < len(values):
        raise IndexError(k)
    arr = values[:]
    lo, hi = 0, len(arr) - 1
    while True:
        pivot = arr[hi]
        i = lo
        for j in range(lo, hi):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[hi] = arr[hi], arr[i]
        if i == k:
            return arr[i]
        if k < i:
            hi = i - 1
        else:
            lo = i + 1


if __name__ == "__main__":
    data = [3, 2, 1, 5, 6, 4]
    assert [quickselect(data, k) for k in range(len(data))] == sorted(data)
    print("quickselect ok")
