"""Slab allocator: cache fixed-size objects to avoid fragmentation."""
from dataclasses import dataclass, field


@dataclass
class SlabCache:
    object_size: int
    objects_per_slab: int
    slabs: list[list[int]] = field(default_factory=list)
    free_list: list[int] = field(default_factory=list)

    def allocate(self) -> int:
        if not self.free_list:
            base = len(self.slabs) * self.objects_per_slab * self.object_size
            self.slabs.append(list(range(base, base + self.objects_per_slab * self.object_size, self.object_size)))
            self.free_list.extend(reversed(self.slabs[-1]))
        return self.free_list.pop()

    def deallocate(self, offset: int) -> None:
        self.free_list.append(offset)

    def utilization(self) -> float:
        total = len(self.slabs) * self.objects_per_slab
        return (total - len(self.free_list)) / total if total else 0.0


if __name__ == "__main__":
    cache = SlabCache(object_size=32, objects_per_slab=8)
    offsets = [cache.allocate() for _ in range(5)]
    assert offsets[0] == 0 and offsets[1] == 32
    cache.deallocate(offsets[0])
    assert cache.utilization() < 1
    print("slab allocator ok")
