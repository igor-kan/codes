"""Base-and-bounds address translation simulation."""
from dataclasses import dataclass


class OutOfBounds(Exception):
    pass


@dataclass
class BaseBounds:
    base: int
    bounds: int

    def translate(self, virtual_address: int) -> int:
        if virtual_address < 0 or virtual_address >= self.bounds:
            raise OutOfBounds(f"address {virtual_address} outside [0, {self.bounds})")
        return self.base + virtual_address


if __name__ == "__main__":
    mmu = BaseBounds(base=32 * 1024, bounds=16 * 1024)
    assert mmu.translate(0) == 32 * 1024
    assert mmu.translate(16 * 1024 - 1) == 32 * 1024 + 16 * 1024 - 1
    try:
        mmu.translate(16 * 1024)
    except OutOfBounds:
        pass
    else:
        raise AssertionError("expected out of bounds")
    print("base/bounds ok")
