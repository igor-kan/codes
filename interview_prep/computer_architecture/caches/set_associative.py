"""Set-associative cache with LRU replacement."""
from collections import OrderedDict
from dataclasses import dataclass, field


@dataclass
class SetAssociativeCache:
    num_sets: int
    ways: int
    block_size: int
    sets: list = field(default_factory=list)
    hits: int = 0
    misses: int = 0

    def __post_init__(self) -> None:
        self.sets = [OrderedDict() for _ in range(self.num_sets)]

    def _split(self, address: int) -> tuple[int, int]:
        block = address // self.block_size
        return block // self.num_sets, block % self.num_sets

    def access(self, address: int) -> bool:
        tag, index = self._split(address)
        way = self.sets[index]
        if tag in way:
            way.move_to_end(tag)
            self.hits += 1
            return True
        self.misses += 1
        way[tag] = True
        if len(way) > self.ways:
            way.popitem(last=False)
        return False


if __name__ == "__main__":
    cache = SetAssociativeCache(num_sets=4, ways=2, block_size=16)
    for address in (0, 64, 0, 64):
        cache.access(address)
    assert cache.hits >= 1
    print(f"hits={cache.hits} misses={cache.misses}")
