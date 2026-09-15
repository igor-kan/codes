"""Per-thread approximate counter with periodic flushes."""
from dataclasses import dataclass, field
import threading


@dataclass
class ApproximateCounter:
    threshold: int = 1000
    global_count: int = 0
    local: dict[int, int] = field(default_factory=dict)
    lock: threading.Lock = field(default_factory=threading.Lock)

    def increment(self, thread_id: int) -> None:
        self.local[thread_id] = self.local.get(thread_id, 0) + 1
        if self.local[thread_id] >= self.threshold:
            self.flush(thread_id)

    def flush(self, thread_id: int) -> None:
        with self.lock:
            self.global_count += self.local.get(thread_id, 0)
        self.local[thread_id] = 0

    def count(self) -> int:
        with self.lock:
            return self.global_count + sum(self.local.values())


if __name__ == "__main__":
    counter = ApproximateCounter(threshold=50)

    def worker(thread_id: int) -> None:
        for _ in range(1000):
            counter.increment(thread_id)

    threads = [threading.Thread(target=worker, args=(i,)) for i in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert counter.count() == 4000
    print("approximate counter ok")
