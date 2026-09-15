"""Shared trace runner for page-replacement policies."""
from collections import OrderedDict


def run_policy(policy: str, pages: list[int], frames: int, future: list[int] | None = None) -> int:
    faults = 0
    if policy == "opt":
        resident: set[int] = set()
        for i, page in enumerate(pages):
            if page in resident:
                continue
            faults += 1
            if len(resident) < frames:
                resident.add(page)
            else:
                lookahead = pages[i + 1:]
                victim = max(resident, key=lambda p: lookahead.index(p) if p in lookahead else float("inf"))
                resident.discard(victim)
                resident.add(page)
        return faults

    resident: "OrderedDict[int, None]" = OrderedDict()
    for page in pages:
        if page in resident:
            if policy == "lru":
                resident.move_to_end(page)
            continue
        faults += 1
        if len(resident) == frames:
            if policy == "fifo":
                resident.popitem(last=False)
            elif policy == "lru":
                resident.popitem(last=False)
            elif policy == "clock":
                resident.popitem(last=False)
        resident[page] = None
    return faults


def compare(pages: list[int], frames: int) -> dict[str, int]:
    return {p: run_policy(p, pages, frames) for p in ("opt", "fifo", "lru", "clock")}


if __name__ == "__main__":
    trace = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    results = compare(trace, frames=3)
    assert results["opt"] <= results["fifo"]
    print(results)
