"""Intro sort: quicksort with heapsort fallback at a depth limit."""
import heapq


def _heap_sort(a: list) -> list:
    heap = list(a)
    heapq.heapify(heap)
    return [heapq.heappop(heap) for _ in range(len(heap))]


def intro_sort(a: list, depth: int | None = None) -> list:
    a = list(a)
    if depth is None:
        depth = 2 * max(1, len(a)).bit_length()
    if len(a) <= 16:
        return sorted(a)
    if depth == 0:
        return _heap_sort(a)
    pivot = a[len(a) // 2]
    lower = [x for x in a if x < pivot]
    equal = [x for x in a if x == pivot]
    upper = [x for x in a if x > pivot]
    return intro_sort(lower, depth - 1) + equal + intro_sort(upper, depth - 1)


if __name__ == "__main__":
    data = [3, 7, 1, 9, 2, 8, 5, 4, 6]
    assert intro_sort(data) == sorted(data)
    print("intro sort ok")
