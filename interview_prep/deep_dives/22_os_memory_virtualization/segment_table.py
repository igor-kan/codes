"""Segment selection and free-space view of physical memory."""
from dataclasses import dataclass


@dataclass
class SegmentTable:
    code: tuple[int, int]
    heap: tuple[int, int]
    stack: tuple[int, int]

    def resolve(self, region: str, offset: int) -> int:
        base, size = getattr(self, region)
        if not 0 <= offset < size:
            raise ValueError(f"{region} offset out of range")
        return base + offset

    def physical_map(self) -> dict[str, tuple[int, int]]:
        return {"code": self.code, "heap": self.heap, "stack": self.stack}

    def holes(self, total: int) -> list[tuple[int, int]]:
        used = sorted(self.physical_map().values())
        holes = []
        cursor = 0
        for base, size in used:
            if base > cursor:
                holes.append((cursor, base - cursor))
            cursor = max(cursor, base + size)
        if cursor < total:
            holes.append((cursor, total - cursor))
        return holes


if __name__ == "__main__":
    table = SegmentTable(code=(0, 0x1000), heap=(0x4000, 0x1000), stack=(0x8000, 0x1000))
    assert table.resolve("heap", 0x10) == 0x4010
    assert (0x1000, 0x3000) in table.holes(0x10000)
    print("segment table ok")
