"""Belady's optimal replacement (farthest future use)."""


def opt(pages: list[int], frames: int) -> int:
    resident: list[int] = []
    faults = 0
    for i, page in enumerate(pages):
        if page in resident:
            continue
        faults += 1
        if len(resident) < frames:
            resident.append(page)
            continue
        future = pages[i + 1:]
        victim = max(resident, key=lambda p: future.index(p) if p in future else float("inf"))
        resident[resident.index(victim)] = page
    return faults


if __name__ == "__main__":
    trace = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    assert opt(trace, 3) == 7
    print("opt faults:", opt(trace, 3))
