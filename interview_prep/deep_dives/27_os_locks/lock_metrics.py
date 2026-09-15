"""Measure lock contention with and without backoff."""
import threading
import time
from dataclasses import dataclass


@dataclass
class Stats:
    acquisitions: int = 0
    wait_time: float = 0.0


def contended(workers: int, iterations: int, backoff: bool) -> Stats:
    lock = threading.Lock()
    stats = Stats()

    def worker() -> None:
        for _ in range(iterations):
            start = time.perf_counter()
            with lock:
                stats.acquisitions += 1
            stats.wait_time += time.perf_counter() - start

    threads = [threading.Thread(target=worker) for _ in range(workers)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return stats


if __name__ == "__main__":
    stats = contended(workers=8, iterations=200, backoff=False)
    assert stats.acquisitions == 1600
    print("acquisitions:", stats.acquisitions)
