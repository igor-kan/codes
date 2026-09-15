"""Worst-fit allocation."""
from dataclasses import dataclass


@dataclass
class Block:
    start: int
    size: int
    free: bool = True


class WorstFitAllocator:
    def __init__(self, size: int) -> None:
        self.blocks = [Block(0, size)]

    def allocate(self, size: int) -> int | None:
        candidates = [i for i, b in enumerate(self.blocks) if b.free and b.size >= size]
        if not candidates:
            return None
        index = max(candidates, key=lambda i: self.blocks[i].size)
        block = self.blocks[index]
        if block.size > size:
            self.blocks.insert(index + 1, Block(block.start + size, block.size - size))
            block.size = size
        block.free = False
        return block.start


if __name__ == "__main__":
    allocator = WorstFitAllocator(100)
    first = allocator.allocate(10)
    second = allocator.allocate(10)
    assert first == 0 and second == 10
    assert allocator.blocks[-1].size == 80
    print("worst fit ok")
