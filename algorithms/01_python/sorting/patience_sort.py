"""Patience sorting: pile-based O(n log n) sort."""
import heapq


def patience_sort(values: list[int]) -> list[int]:
    piles: list[list[int]] = []
    for value in values:
        for pile in piles:
            if pile[-1] >= value:
                pile.append(value)
                break
        else:
            piles.append([value])

    heap = [(pile[-1], i) for i, pile in enumerate(piles)]
    heapq.heapify(heap)
    result: list[int] = []
    while heap:
        value, index = heapq.heappop(heap)
        result.append(value)
        piles[index].pop()
        if piles[index]:
            heapq.heappush(heap, (piles[index][-1], index))
    return result


if __name__ == "__main__":
    data = [4, 2, 5, 1, 3, 6]
    assert patience_sort(data) == sorted(data)
    print("patience sort ok")
