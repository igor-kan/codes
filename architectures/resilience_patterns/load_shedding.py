"""Load shedding: drop low-priority work when over capacity."""
from collections import deque


class LoadShedder:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.queue: deque[tuple[int, str]] = deque()
        self.accepted = 0
        self.shed = 0

    def submit(self, priority: int, work: str) -> bool:
        if len(self.queue) >= self.capacity:
            if priority > 0:
                lowest = min(self.queue, key=lambda item: item[0])
                if lowest[0] < priority:
                    self.queue.remove(lowest)
                    self.queue.append((priority, work))
                    self.shed += 1
                    return True
            self.shed += 1
            return False
        self.queue.append((priority, work))
        self.accepted += 1
        return True


if __name__ == "__main__":
    shedder = LoadShedder(capacity=2)
    assert shedder.submit(0, "a") and shedder.submit(0, "b")
    assert not shedder.submit(0, "c")          # queue full, same priority -> shed
    assert shedder.submit(5, "urgent")          # preempts low priority
    print("load shedding ok")
