"""Demonstrate Belady's anomaly with FIFO."""
from collections import deque


def fifo_faults(pages: list[int], frames: int) -> int:
    queue: deque[int] = deque()
    resident: set[int] = set()
    faults = 0
    for page in pages:
        if page in resident:
            continue
        faults += 1
        if len(resident) == frames:
            resident.discard(queue.popleft())
        queue.append(page)
        resident.add(page)
    return faults


def is_anomalous(pages: list[int]) -> bool:
    return any(fifo_faults(pages, f) < fifo_faults(pages, f + 1) for f in range(1, 6))


if __name__ == "__main__":
    trace = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    assert is_anomalous(trace)
    print("Belady's anomaly detected")
