"""Bitonic sort: a parallel-friendly sorting network."""
def _bitonic_merge(a: list, low: int, count: int, ascending: bool) -> None:
    if count > 1:
        k = count // 2
        for i in range(low, low + k):
            if (a[i] > a[i + k]) == ascending:
                a[i], a[i + k] = a[i + k], a[i]
        _bitonic_merge(a, low, k, ascending)
        _bitonic_merge(a, low + k, k, ascending)


def _bitonic_sort(a: list, low: int, count: int, ascending: bool) -> None:
    if count > 1:
        k = count // 2
        _bitonic_sort(a, low, k, True)
        _bitonic_sort(a, low + k, k, False)
        _bitonic_merge(a, low, count, ascending)


def bitonic_sort(a: list) -> list:
    original = len(a)
    n = 1
    while n < original:
        n *= 2
    a = list(a) + [float("inf")] * (n - original)
    _bitonic_sort(a, 0, n, True)
    return a[:original]


if __name__ == "__main__":
    data = [3, 7, 4, 8, 6, 2, 1, 5]
    assert bitonic_sort(data) == sorted(data)
    print("bitonic sort ok")
