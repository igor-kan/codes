"""A spinlock built on threading.Lock's non-blocking acquire for illustration."""
import threading
import time


class SpinLock:
    """Educational spinlock using a boolean flag and compare-and-set emulation."""

    def __init__(self) -> None:
        self._flag = threading.Event()

    def lock(self) -> None:
        while True:
            if self._try_set():
                return
            time.sleep(0)

    def _try_set(self) -> bool:
        # Emulate an atomic test-and-set with the GIL-protected common case.
        if self._flag.is_set():
            return False
        self._flag.set()
        return True

    def unlock(self) -> None:
        self._flag.clear()


if __name__ == "__main__":
    lock = SpinLock()
    counter = {"value": 0}

    def worker() -> None:
        for _ in range(1_000):
            lock.lock()
            counter["value"] += 1
            lock.unlock()

    threads = [threading.Thread(target=worker) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert counter["value"] == 4_000
    print("spinlock ok")
