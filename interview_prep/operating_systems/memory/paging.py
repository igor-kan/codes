"""Paging: virtual-to-physical translation with a page table."""
from dataclasses import dataclass, field

PAGE_SIZE = 4096


@dataclass
class PageTable:
    entries: dict[int, int | None] = field(default_factory=dict)

    def map(self, page: int, frame: int) -> None:
        self.entries[page] = frame

    def translate(self, virtual_address: int) -> int:
        page, offset = divmod(virtual_address, PAGE_SIZE)
        frame = self.entries.get(page)
        if frame is None:
            raise KeyError(f"page {page} not present")
        return frame * PAGE_SIZE + offset

    def split(self, virtual_address: int) -> tuple[int, int]:
        return divmod(virtual_address, PAGE_SIZE)


if __name__ == "__main__":
    table = PageTable()
    table.map(0, 5)
    table.map(1, 2)
    assert table.translate(0) == 5 * PAGE_SIZE
    assert table.translate(PAGE_SIZE + 10) == 2 * PAGE_SIZE + 10
    assert table.split(9000) == (2, 9000 - 2 * PAGE_SIZE)
    print("paging ok")
