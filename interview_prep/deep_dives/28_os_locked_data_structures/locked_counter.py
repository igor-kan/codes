"""Scalable counters: locked, striped and approximate."""
import threading
from dataclasses import dataclass, field


class LockedCounter:
    def __init__(self) -> None:
        self.value = 0
        self.lock = threading.Lock()

    def add(self, delta: int = 1) -> None:
        with self.lock:
            self.value += delta

    def get(self) -> int:
        with self.lock:
            return self.value


class StripedCounter:
    def __init__(self, stripes: int = 8) -> None:
        self.locks = [threading.Lock() for _ in range(stripes)]
        self.values = [0] * stripes

    def add(self, delta: int, stripe: int) -> None:
        with self.locks[stripe % len(self.locks)]:
            self.values[stripe % len(self.values)] += delta

    def get(self) -> int:
        return sum(self.values)


@dataclass
class ApproximateCounter:
    threshold: int = 100
    global_value: int = 0
    local: dict[int, int] = field(default_factory=dict)
    lock: threading.Lock = field(default_factory=threading.Lock)

    def add(self, thread_id: int) -> None:
        self.local[thread_id] = self.local.get(thread_id, 0) + 1
        if self.local[thread_id] >= self.threshold:
            with self.lock:
                self.global_value += self.local[thread_id]
            self.local[thread_id] = 0

    def get(self) -> int:
        with self.lock:
            return self.global_value + sum(self.local.values())


if __name__ == "__main__":
    counter = LockedCounter()
    counter.add(5)
    assert counter.get() == 5

    striped = StripedCounter()
    for i in range(100):
        striped.add(1, i)
    assert striped.get() == 100
    print("locked counters ok")
