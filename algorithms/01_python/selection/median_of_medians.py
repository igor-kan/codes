"""Deterministic linear-time selection (CLRS 9.3, median of medians)."""


def _partition(arr: list[int], pivot: int) -> tuple[int, int]:
    i = 0
    for j in range(len(arr)):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    k = i
    for j in range(k, len(arr)):
        if arr[j] == pivot:
            arr[k], arr[j] = arr[j], arr[k]
            k += 1
    return i, k


def select(values: list[int], k: int) -> int:
    arr = values[:]
    if len(arr) <= 5:
        return sorted(arr)[k]
    chunks = [sorted(arr[i:i + 5]) for i in range(0, len(arr), 5)]
    medians = [chunk[len(chunk) // 2] for chunk in chunks]
    pivot = select(medians, len(medians) // 2)
    left, right = _partition(arr, pivot)
    if k < left:
        return select(arr[:left], k)
    if k < right:
        return pivot
    return select(arr[right:], k - right)


if __name__ == "__main__":
    data = [7, 1, 9, 4, 2, 8, 3, 6, 5, 0]
    assert [select(data, k) for k in range(len(data))] == sorted(data)
    print("median of medians ok")
