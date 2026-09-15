"""Compare base/bounds, segmentation and paging translation on one address."""
PAGE_SIZE = 4096


def base_bounds(address: int, base: int, limit: int) -> int:
    if address >= limit:
        raise ValueError("out of bounds")
    return base + address


def segmented(address: int, segment: tuple[int, int, int]) -> int:
    base, size, offset_start = segment
    offset = address - offset_start
    if not 0 <= offset < size:
        raise ValueError("segment violation")
    return base + offset


def paged(address: int, page_table: dict[int, int]) -> int:
    page, offset = divmod(address, PAGE_SIZE)
    return page_table[page] * PAGE_SIZE + offset


if __name__ == "__main__":
    assert base_bounds(0x100, 0x10000, 0x1000) == 0x10100
    assert segmented(0x1010, (0x4000, 0x1000, 0x1000)) == 0x4010
    assert paged(0x3010, {0: 1, 1: 4, 2: 6, 3: 8}) == 8 * PAGE_SIZE + 0x10
    print("translation schemes ok")
