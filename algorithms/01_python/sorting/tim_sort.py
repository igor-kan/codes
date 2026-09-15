"""Tim sort: insertion sort on runs, then merge."""
RUN = 32


def insertion_sort(a: list, lo: int, hi: int) -> None:
    for i in range(lo + 1, hi):
        key, j = a[i], i - 1
        while j >= lo and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


def merge(a: list, lo: int, mid: int, hi: int) -> None:
    left, right = a[lo:mid], a[mid:hi]
    i = j = 0
    k = lo
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[k], i = left[i], i + 1
        else:
            a[k], j = right[j], j + 1
        k += 1
    while i < len(left):
        a[k], i, k = left[i], i + 1, k + 1
    while j < len(right):
        a[k], j, k = right[j], j + 1, k + 1


def tim_sort(a: list) -> list:
    a = list(a)
    n = len(a)
    for lo in range(0, n, RUN):
        insertion_sort(a, lo, min(lo + RUN, n))
    size = RUN
    while size < n:
        for lo in range(0, n, 2 * size):
            merge(a, lo, min(lo + size, n), min(lo + 2 * size, n))
        size *= 2
    return a


if __name__ == "__main__":
    data = [5, 21, 7, 23, 19, 3, 8, 1, 40]
    assert tim_sort(data) == sorted(data)
    print("tim sort ok")
