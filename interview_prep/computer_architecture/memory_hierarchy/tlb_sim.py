"""TLB and page-walk cost simulation."""
from collections import OrderedDict


class AddressTranslation:
    def __init__(self, tlb_size: int, page_walk_cost: int, tlb_hit_cost: int = 1) -> None:
        self.tlb: OrderedDict[int, int] = OrderedDict()
        self.tlb_size = tlb_size
        self.page_walk_cost = page_walk_cost
        self.tlb_hit_cost = tlb_hit_cost
        self.cycles = 0
        self.hits = 0
        self.misses = 0

    def translate(self, page: int) -> int:
        if page in self.tlb:
            self.tlb.move_to_end(page)
            self.cycles += self.tlb_hit_cost
            self.hits += 1
            return self.tlb[page]
        self.cycles += self.page_walk_cost
        self.misses += 1
        self.tlb[page] = page * 4  # fake frame
        if len(self.tlb) > self.tlb_size:
            self.tlb.popitem(last=False)
        return self.tlb[page]


if __name__ == "__main__":
    mmu = AddressTranslation(tlb_size=16, page_walk_cost=100)
    for page in range(16):
        mmu.translate(page)
    for page in range(16):
        mmu.translate(page)
    assert mmu.hits == 16 and mmu.misses == 16
    print(f"avg cycles/access: {mmu.cycles / (mmu.hits + mmu.misses):.1f}")
