"""TLB with LRU replacement and effective access time."""
from collections import OrderedDict


class TLB:
    def __init__(self, capacity: int, hit_cost: int = 1, miss_cost: int = 50) -> None:
        self.capacity = capacity
        self.entries: OrderedDict[int, int] = OrderedDict()
        self.hit_cost = hit_cost
        self.miss_cost = miss_cost
        self.hits = 0
        self.misses = 0
        self.cycles = 0

    def translate(self, page: int, page_table: dict[int, int]) -> int:
        if page in self.entries:
            self.entries.move_to_end(page)
            self.hits += 1
            self.cycles += self.hit_cost
            return self.entries[page]
        self.misses += 1
        self.cycles += self.miss_cost
        self.entries[page] = page_table[page]
        if len(self.entries) > self.capacity:
            self.entries.popitem(last=False)
        return page_table[page]

    @property
    def hit_rate(self) -> float:
        total = self.hits + self.misses
        return self.hits / total if total else 0.0


if __name__ == "__main__":
    page_table = {i: i for i in range(64)}
    tlb = TLB(capacity=8)
    for page in [0, 1, 2, 3, 4, 5, 6, 7, 0, 1]:
        tlb.translate(page, page_table)
    assert tlb.hits == 2
    print(f"tlb hit rate: {tlb.hit_rate:.2f}")
