"""TLB simulation with LRU replacement and hit/miss accounting."""
from collections import OrderedDict


class TLB:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.entries: OrderedDict[int, int] = OrderedDict()
        self.hits = 0
        self.misses = 0

    def lookup(self, page: int, page_table: dict[int, int]) -> int:
        if page in self.entries:
            self.hits += 1
            self.entries.move_to_end(page)
            return self.entries[page]
        self.misses += 1
        frame = page_table[page]
        self.entries[page] = frame
        self.entries.move_to_end(page)
        if len(self.entries) > self.capacity:
            self.entries.popitem(last=False)
        return frame

    @property
    def hit_rate(self) -> float:
        total = self.hits + self.misses
        return self.hits / total if total else 0.0


if __name__ == "__main__":
    page_table = {i: i * 3 for i in range(100)}
    tlb = TLB(4)
    for page in [1, 2, 3, 4, 1, 1, 5]:
        tlb.lookup(page, page_table)
    assert tlb.hits == 2
    assert 0 < tlb.hit_rate < 1
    print(f"hit rate: {tlb.hit_rate:.2f}")
