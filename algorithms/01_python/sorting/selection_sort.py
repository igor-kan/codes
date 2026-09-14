"""Selection sort."""

from typing import List


def selection_sort(arr: List[int]) -> List[int]:
    a = arr[:]
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


if __name__ == "__main__":
    assert selection_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]
    assert selection_sort([]) == []
    assert selection_sort([1]) == [1]
    assert selection_sort([3, 2, 1]) == [1, 2, 3]
    print("[Python SelectionSort] verified.")
