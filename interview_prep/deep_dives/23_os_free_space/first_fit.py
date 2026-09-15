"""First-fit allocation over a free list."""
from dataclasses import dataclass


@dataclass
class Block:
    start: int
    size: int
    free: bool = True


class FirstFitAllocator:
    def __init__(self, size: int) -> None:
        self.blocks = [Block(0, size)]

    def allocate(self, size: int) -> int | None:
        for i, block in enumerate(self.blocks):
            if block.free and block.size >= size:
                if block.size > size:
                    self.blocks.insert(i + 1, Block(block.start + size, block.size - size))
                    block.size = size
                block.free = False
                return block.start
        return None

    def free(self, start: int) -> None:
        for block in self.blocks:
            if block.start == start:
                block.free = True
                break
        self.coalesce()

    def coalesce(self) -> None:
        merged: list[Block] = []
        for block in self.blocks:
            if merged and merged[-1].free and block.free:
                merged[-1].size += block.size
            else:
                merged.append(block)
        self.blocks = merged


if __name__ == "__main__":
    allocator = FirstFitAllocator(100)
    a = allocator.allocate(20)
    b = allocator.allocate(30)
    assert a == 0 and b == 20
    allocator.free(a)
    assert allocator.blocks[0].size == 20
    print("first fit ok")
