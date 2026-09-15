"""A test-and-set spinlock built on threading.Lock's fast path."""
import threading
import time


class SpinLock:
    def __init__(self) -> None:
        self._flag = False
        self._guard = threading.Lock()

    def _test_and_set(self) -> bool:
        with self._guard:  # emulates the atomic primitive under the GIL
            old = self._flag
            self._flag = True
            return old

    def lock(self) -> None:
        while self._test_and_set():
            time.sleep(0)

    def unlock(self) -> None:
        with self._guard:
            self._flag = False


if __name__ == "__main__":
    lock = SpinLock()
    counter = [0]

    def bump() -> None:
        for _ in range(2000):
            lock.lock()
            counter[0] += 1
            lock.unlock()

    threads = [threading.Thread(target=bump) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert counter[0] == 8000
    print("spinlock ok")
