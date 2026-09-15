"""Atomic counters using locks and itertools.count (GIL-atomic)."""
import itertools
import threading


class LockedCounter:
    def __init__(self) -> None:
        self.value = 0
        self.lock = threading.Lock()

    def increment(self) -> int:
        with self.lock:
            self.value += 1
            return self.value


class AtomicCounter:
    def __init__(self) -> None:
        self.counter = itertools.count()
        self.value = 0

    def increment(self) -> int:
        self.value = next(self.counter)
        return self.value


if __name__ == "__main__":
    counter = LockedCounter()
    final = []
    threads = [threading.Thread(target=lambda: [counter.increment() for _ in range(1000)]) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert counter.value == 4000
    print("atomic counter ok")
