"""O(1) LFU cache using frequency buckets."""
from collections import OrderedDict, defaultdict


class LFUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.min_freq = 0
        self.values: dict[int, int] = {}
        self.freqs: dict[int, int] = {}
        self.buckets: dict[int, OrderedDict] = defaultdict(OrderedDict)

    def _touch(self, key: int) -> None:
        freq = self.freqs[key]
        del self.buckets[freq][key]
        if not self.buckets[freq] and self.min_freq == freq:
            self.min_freq += 1
        self.freqs[key] = freq + 1
        self.buckets[freq + 1][key] = None

    def get(self, key: int) -> int:
        if key not in self.values:
            return -1
        self._touch(key)
        return self.values[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        if key in self.values:
            self.values[key] = value
            self._touch(key)
            return
        if len(self.values) >= self.capacity:
            evicted, _ = self.buckets[self.min_freq].popitem(last=False)
            del self.values[evicted]
            del self.freqs[evicted]
        self.values[key] = value
        self.freqs[key] = 1
        self.buckets[1][key] = None
        self.min_freq = 1


if __name__ == "__main__":
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)          # evicts key 2 (least frequent)
    assert cache.get(2) == -1
    print("lfu cache ok")
