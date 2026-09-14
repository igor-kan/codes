"""Direct-mapped cache address decomposition and hit/miss stats."""
from dataclasses import dataclass, field


@dataclass
class DirectMappedCache:
    num_lines: int
    block_size: int
    tags: list[int | None] = field(default_factory=list)
    hits: int = 0
    misses: int = 0

    def __post_init__(self) -> None:
        self.tags = [None] * self.num_lines

    def _split(self, address: int) -> tuple[int, int, int]:
        offset = address % self.block_size
        block = address // self.block_size
        return block // self.num_lines, block % self.num_lines, offset

    def access(self, address: int) -> bool:
        tag, index, _ = self._split(address)
        if self.tags[index] == tag:
            self.hits += 1
            return True
        self.misses += 1
        self.tags[index] = tag
        return False


if __name__ == "__main__":
    cache = DirectMappedCache(num_lines=8, block_size=16)
    assert cache.access(0x00) is False       # cold miss
    assert cache.access(0x04) is True        # same line
    assert cache.access(0x80) is False       # same index, different tag
    assert cache.access(0x00) is False       # evicted
    print(f"hits={cache.hits} misses={cache.misses}")
