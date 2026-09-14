"""Insertion sort."""

from typing import List


def insertion_sort(arr: List[int]) -> List[int]:
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


if __name__ == "__main__":
    assert insertion_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]
    assert insertion_sort([]) == []
    assert insertion_sort([1]) == [1]
    assert insertion_sort([3, 2, 1]) == [1, 2, 3]
    print("[Python InsertionSort] verified.")
