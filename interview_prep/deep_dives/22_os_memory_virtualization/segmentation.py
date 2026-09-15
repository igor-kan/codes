"""Segmented address translation with per-segment protection."""
from dataclasses import dataclass, field


@dataclass
class Segment:
    base: int
    size: int
    readable: bool = True
    writable: bool = True
    executable: bool = False


class SegmentTable:
    def __init__(self) -> None:
        self.segments: dict[str, Segment] = {}

    def add(self, name: str, segment: Segment) -> None:
        self.segments[name] = segment

    def translate(self, segment_name: str, offset: int, access: str = "read") -> int:
        segment = self.segments[segment_name]
        if offset >= segment.size:
            raise ValueError("offset beyond segment")
        if access == "write" and not segment.writable:
            raise PermissionError("segment not writable")
        if access == "exec" and not segment.executable:
            raise PermissionError("segment not executable")
        return segment.base + offset


if __name__ == "__main__":
    table = SegmentTable()
    table.add("code", Segment(0, 0x2000, writable=False, executable=True))
    table.add("heap", Segment(0x10000, 0x8000, executable=False))
    assert table.translate("code", 0x10, "exec") == 0x10
    assert table.translate("heap", 0x100) == 0x10100
    try:
        table.translate("code", 0x10, "write")
    except PermissionError:
        pass
    else:
        raise AssertionError("expected permission error")
    print("segmentation ok")
