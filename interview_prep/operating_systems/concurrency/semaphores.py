"""Counting semaphores built on threading primitives."""
import threading


class Semaphore:
    def __init__(self, value: int) -> None:
        self.value = value
        self.mutex = threading.Lock()
        self.cond = threading.Condition(self.mutex)

    def acquire(self) -> None:
        with self.mutex:
            while self.value == 0:
                self.cond.wait()
            self.value -= 1

    def release(self) -> None:
        with self.mutex:
            self.value += 1
            self.cond.notify()


if __name__ == "__main__":
    semaphore = Semaphore(2)
    active = 0
    peak = 0

    def worker() -> None:
        global active, peak
        semaphore.acquire()
        active += 1
        peak = max(peak, active)
        active -= 1
        semaphore.release()

    threads = [threading.Thread(target=worker) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert peak <= 2
    print("semaphore ok, peak concurrency:", peak)
