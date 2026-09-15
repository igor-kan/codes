"""Walk a multi-level (two-level) page table."""
from dataclasses import dataclass, field

PAGE_SHIFT = 12
PTE_PER_TABLE = 4  # small for demonstration


@dataclass
class TwoLevelPageTable:
    directories: dict[int, dict[int, int]] = field(default_factory=dict)

    def map(self, virtual_page: int, frame: int) -> None:
        directory, table_index = divmod(virtual_page, PTE_PER_TABLE)
        self.directories.setdefault(directory, {})[table_index] = frame

    def translate(self, address: int) -> int:
        virtual_page, offset = divmod(address, 1 << PAGE_SHIFT)
        directory, table_index = divmod(virtual_page, PTE_PER_TABLE)
        if directory not in self.directories or table_index not in self.directories[directory]:
            raise KeyError("page fault")
        frame = self.directories[directory][table_index]
        return (frame << PAGE_SHIFT) | offset


if __name__ == "__main__":
    table = TwoLevelPageTable()
    table.map(5, 20)
    assert table.translate((5 << PAGE_SHIFT) | 0x123) == (20 << PAGE_SHIFT) | 0x123
    print("two-level page walk ok")
