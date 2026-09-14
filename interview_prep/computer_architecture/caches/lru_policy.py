"""LRU vs FIFO replacement under the same access stream."""
from collections import OrderedDict


def simulate(policy: str, accesses: list[int], capacity: int) -> int:
    cache: OrderedDict[int, None] = OrderedDict()
    misses = 0
    for block in accesses:
        if block in cache:
            cache.move_to_end(block)
            continue
        misses += 1
        cache[block] = None
        if len(cache) > capacity:
            if policy == "lru":
                cache.popitem(last=False)
            else:  # fifo
                cache.popitem(last=False)
        if policy == "fifo" and block in cache:
            pass
    return misses


def simulate_fifo(accesses: list[int], capacity: int) -> int:
    from collections import deque

    order: deque[int] = deque()
    present: set[int] = set()
    misses = 0
    for block in accesses:
        if block in present:
            continue
        misses += 1
        if len(present) == capacity:
            present.discard(order.popleft())
        order.append(block)
        present.add(block)
    return misses


def simulate_lru(accesses: list[int], capacity: int) -> int:
    cache: OrderedDict[int, None] = OrderedDict()
    misses = 0
    for block in accesses:
        if block in cache:
            cache.move_to_end(block)
            continue
        misses += 1
        cache[block] = None
        if len(cache) > capacity:
            cache.popitem(last=False)
    return misses


if __name__ == "__main__":
    stream = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    assert simulate_lru(stream, 3) <= simulate_fifo(stream, 3) + 1
    print("lru misses:", simulate_lru(stream, 3), "fifo misses:", simulate_fifo(stream, 3))
