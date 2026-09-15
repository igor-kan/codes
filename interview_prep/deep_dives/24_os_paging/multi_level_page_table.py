"""Sparse multi-level page table memory accounting vs a flat table."""
from dataclasses import dataclass


@dataclass
class MultiLevel:
    levels: int
    entries_per_table: int
    page_size: int

    def flat_size_bytes(self, address_bits: int) -> int:
        entries = 2 ** (address_bits - (self.page_size.bit_length() - 1))
        return entries * 8  # 8-byte PTEs

    def sparse_size_bytes(self, mapped_pages: int) -> int:
        # One table per level per mapped page path, plus leaf PTEs.
        return (mapped_pages * self.levels + mapped_pages) * 8


if __name__ == "__main__":
    table = MultiLevel(levels=4, entries_per_table=512, page_size=4096)
    flat = table.flat_size_bytes(48)
    sparse = table.sparse_size_bytes(1000)
    assert sparse < flat
    print(f"flat={flat / 1e9:.1f} GB sparse={sparse / 1e3:.1f} KB for 1000 pages")
