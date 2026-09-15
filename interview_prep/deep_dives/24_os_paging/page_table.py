"""Single-level page table with permission bits."""
from dataclasses import dataclass, field

PAGE_SIZE = 4096


@dataclass
class Entry:
    frame: int | None = None
    writable: bool = True
    executable: bool = False


class PageTable:
    def __init__(self) -> None:
        self.entries: dict[int, Entry] = {}

    def map(self, page: int, frame: int, writable: bool = True, executable: bool = False) -> None:
        self.entries[page] = Entry(frame, writable, executable)

    def translate(self, address: int, access: str = "read") -> int:
        page, offset = divmod(address, PAGE_SIZE)
        entry = self.entries.get(page)
        if entry is None or entry.frame is None:
            raise KeyError(f"page fault at {hex(address)}")
        if access == "write" and not entry.writable:
            raise PermissionError("write to read-only page")
        if access == "exec" and not entry.executable:
            raise PermissionError("execute on non-executable page")
        return entry.frame * PAGE_SIZE + offset


if __name__ == "__main__":
    table = PageTable()
    table.map(0, 5)
    table.map(1, 8, writable=False)
    assert table.translate(10) == 5 * PAGE_SIZE + 10
    try:
        table.translate(PAGE_SIZE + 1, "write")
    except PermissionError:
        pass
    else:
        raise AssertionError("expected permission error")
    print("single-level page table ok")
