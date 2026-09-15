"""Effective access time given TLB hit rate and page-walk cost."""
from dataclasses import dataclass


@dataclass(frozen=True)
class MemorySystem:
    tlb_hit_rate: float
    tlb_hit_latency: float
    page_walk_latency: float
    memory_latency: float

    @property
    def eat(self) -> float:
        hit = self.tlb_hit_latency + self.memory_latency
        miss = self.page_walk_latency + self.memory_latency
        return self.tlb_hit_rate * hit + (1 - self.tlb_hit_rate) * miss


if __name__ == "__main__":
    system = MemorySystem(tlb_hit_rate=0.98, tlb_hit_latency=1, page_walk_latency=20, memory_latency=100)
    assert system.eat < 120
    print(f"effective access time: {system.eat:.2f} ns")
