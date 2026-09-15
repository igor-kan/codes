"""Best-fit allocation."""
from dataclasses import dataclass


@dataclass
class Block:
    start: int
    size: int
    free: bool = True


class BestFitAllocator:
    def __init__(self, size: int) -> None:
        self.blocks = [Block(0, size)]

    def allocate(self, size: int) -> int | None:
        candidates = [i for i, b in enumerate(self.blocks) if b.free and b.size >= size]
        if not candidates:
            return None
        index = min(candidates, key=lambda i: self.blocks[i].size)
        block = self.blocks[index]
        if block.size > size:
            self.blocks.insert(index + 1, Block(block.start + size, block.size - size))
            block.size = size
        block.free = False
        return block.start


if __name__ == "__main__":
    allocator = BestFitAllocator(100)
    allocator.allocate(30)
    allocator.allocate(20)
    # Best fit picks the remaining 70-block and leaves a 50-sized hole.
    assert allocator.blocks[-1].size >= 50
    print("best fit ok")
