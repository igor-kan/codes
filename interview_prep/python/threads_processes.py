"""Threads vs processes vs the GIL."""
import threading
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def io_bound(n: int) -> int:
    return sum(i * i for i in range(n))


def cpu_bound(n: int) -> int:
    return sum(i * i for i in range(n))


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=4) as pool:
        assert list(pool.map(io_bound, [1000, 2000])) == [io_bound(1000), io_bound(2000)]

    with ProcessPoolExecutor(max_workers=2) as pool:
        assert list(pool.map(cpu_bound, [100, 200])) == [cpu_bound(100), cpu_bound(200)]

    counter = {"value": 0}
    lock = threading.Lock()

    def bump() -> None:
        with lock:
            counter["value"] += 1

    threads = [threading.Thread(target=bump) for _ in range(50)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert counter["value"] == 50
    print("ok")
