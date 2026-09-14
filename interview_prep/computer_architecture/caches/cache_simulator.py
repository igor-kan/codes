"""A configurable set-associative cache simulator with statistics."""
from collections import OrderedDict
from dataclasses import dataclass


@dataclass
class Stats:
    accesses: int = 0
    hits: int = 0
    misses: int = 0

    @property
    def hit_rate(self) -> float:
        return self.hits / self.accesses if self.accesses else 0.0


class Cache:
    def __init__(self, size_bytes: int, block_size: int, ways: int) -> None:
        self.block_size = block_size
        self.ways = ways
        self.num_sets = size_bytes // (block_size * ways)
        self.sets = [OrderedDict() for _ in range(self.num_sets)]
        self.stats = Stats()

    def access(self, address: int) -> bool:
        self.stats.accesses += 1
        block = address // self.block_size
        tag, index = block // self.num_sets, block % self.num_sets
        way = self.sets[index]
        if tag in way:
            way.move_to_end(tag)
            self.stats.hits += 1
            return True
        self.stats.misses += 1
        way[tag] = True
        if len(way) > self.ways:
            way.popitem(last=False)
        return False


if __name__ == "__main__":
    cache = Cache(size_bytes=1024, block_size=64, ways=2)
    for _ in range(2):
        for address in range(0, 1024, 64):
            cache.access(address)
    assert cache.stats.hits > 0
    print(f"hit rate over repeated scan: {cache.stats.hit_rate:.2f}")
