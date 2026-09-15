"""Free-list coalescing with boundary tags."""
from dataclasses import dataclass


@dataclass
class Block:
    start: int
    size: int
    free: bool = True


def coalesce(blocks: list[Block]) -> list[Block]:
    merged: list[Block] = []
    for block in sorted(blocks, key=lambda b: b.start):
        if merged and merged[-1].free and block.free and merged[-1].start + merged[-1].size == block.start:
            merged[-1].size += block.size
        else:
            merged.append(Block(block.start, block.size, block.free))
    return merged


if __name__ == "__main__":
    blocks = [Block(0, 10), Block(10, 20), Block(30, 5, free=False), Block(35, 15)]
    result = coalesce(blocks)
    assert len(result) == 3 and result[0].size == 30
    print("coalescing ok:", [(b.start, b.size) for b in result])
