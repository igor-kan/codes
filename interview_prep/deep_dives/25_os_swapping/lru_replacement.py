"""LRU page replacement using an OrderedDict."""
from collections import OrderedDict


def lru(pages: list[int], frames: int) -> int:
    resident: "OrderedDict[int, None]" = OrderedDict()
    faults = 0
    for page in pages:
        if page in resident:
            resident.move_to_end(page)
            continue
        faults += 1
        if len(resident) == frames:
            resident.popitem(last=False)
        resident[page] = None
    return faults


if __name__ == "__main__":
    trace = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    assert lru(trace, 3) == 10
    print("lru faults:", lru(trace, 3))
