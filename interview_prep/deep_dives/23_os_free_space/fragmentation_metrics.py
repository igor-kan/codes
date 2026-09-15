"""Internal and external fragmentation metrics."""
from dataclasses import dataclass


@dataclass
class Allocation:
    requested: int
    granted: int


def internal_fragmentation(allocations: list[Allocation]) -> float:
    granted = sum(a.granted for a in allocations)
    used = sum(a.requested for a in allocations)
    return (granted - used) / granted if granted else 0.0


def external_fragmentation(holes: list[int], largest_request: int) -> float:
    total_free = sum(holes)
    if total_free == 0:
        return 0.0
    allocatable = sum(h for h in holes if h >= largest_request)
    return (total_free - allocatable) / total_free


if __name__ == "__main__":
    assert internal_fragmentation([Allocation(100, 128), Allocation(50, 64)]) > 0
    assert external_fragmentation([16, 16, 16], 64) == 1.0
    print("fragmentation metrics ok")
