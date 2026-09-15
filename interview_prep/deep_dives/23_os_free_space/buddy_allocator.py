"""Power-of-two buddy allocator."""
from dataclasses import dataclass, field


class BuddyAllocator:
    def __init__(self, size: int) -> None:
        self.size = size
        self.free: dict[int, set[int]] = {}
        self._add(size, 0)

    def _add(self, size: int, offset: int) -> None:
        self.free.setdefault(size, set()).add(offset)

    def _next_power_of_two(self, size: int) -> int:
        power = 1
        while power < size:
            power *= 2
        return power

    def allocate(self, size: int) -> int | None:
        request = self._next_power_of_two(max(size, 1))
        block = request
        while block <= self.size and not self.free.get(block):
            block *= 2
        if block > self.size:
            return None
        offset = self.free[block].pop()
        while block > request:
            block //= 2
            self._add(block, offset + block)
        return offset

    def deallocate(self, offset: int, size: int) -> None:
        block = self._next_power_of_two(size)
        while block < self.size:
            buddy = offset ^ block
            if buddy in self.free.get(block, set()):
                self.free[block].discard(buddy)
                offset = min(offset, buddy)
                block *= 2
            else:
                break
        self._add(block, offset)


if __name__ == "__main__":
    allocator = BuddyAllocator(64)
    offset = allocator.allocate(10)  # rounds to 16
    assert offset == 0
    allocator.deallocate(offset, 16)
    assert 0 in allocator.free[64]
    print("buddy allocator ok")
