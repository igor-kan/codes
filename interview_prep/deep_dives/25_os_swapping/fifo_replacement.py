"""FIFO page replacement and Belady's anomaly."""
from collections import deque


def fifo(pages: list[int], frames: int) -> int:
    queue: deque[int] = deque()
    resident: set[int] = set()
    faults = 0
    for page in pages:
        if page in resident:
            continue
        faults += 1
        if len(resident) == frames:
            victim = queue.popleft()
            resident.discard(victim)
        queue.append(page)
        resident.add(page)
    return faults


if __name__ == "__main__":
    # Classic trace where more frames cause more faults (Belady's anomaly).
    trace = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    assert fifo(trace, 3) == 9
    assert fifo(trace, 4) == 10
    print("fifo 3 frames:", fifo(trace, 3), "4 frames:", fifo(trace, 4))
