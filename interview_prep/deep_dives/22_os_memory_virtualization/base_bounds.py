"""Base-and-bounds translation with relocation."""
from dataclasses import dataclass


class SegmentationFault(Exception):
    pass


@dataclass
class BaseBounds:
    base: int
    limit: int

    def translate(self, virtual_address: int) -> int:
        if not 0 <= virtual_address < self.limit:
            raise SegmentationFault(f"address {virtual_address} out of bounds")
        return self.base + virtual_address

    def translate_checked(self, virtual_address: int, access: str = "read") -> int:
        if access == "exec" and virtual_address >= self.limit:
            raise SegmentationFault("exec beyond limit")
        return self.translate(virtual_address)


if __name__ == "__main__":
    mmu = BaseBounds(base=0x10000, limit=0x4000)
    assert mmu.translate(0) == 0x10000
    assert mmu.translate(0x3FFF) == 0x13FFF
    try:
        mmu.translate(0x4000)
    except SegmentationFault:
        pass
    else:
        raise AssertionError("expected fault")
    print("base/bounds ok")
