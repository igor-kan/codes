"""Measure thread creation cost vs a thread pool."""
import threading
import time
from concurrent.futures import ThreadPoolExecutor


def task() -> int:
    return sum(range(1000))


def with_threads(n: int) -> tuple[int, float]:
    start = time.perf_counter()
    results = []
    threads = [threading.Thread(target=lambda: results.append(task())) for _ in range(n)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return len(results), time.perf_counter() - start


def with_pool(n: int) -> tuple[int, float]:
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(lambda _: task(), range(n)))
    return len(results), time.perf_counter() - start


if __name__ == "__main__":
    assert with_threads(50)[0] == 50
    assert with_pool(50)[0] == 50
    print("thread creation ok")
