"""Counting semaphore with wait/post."""
import threading


class Semaphore:
    def __init__(self, value: int) -> None:
        self.value = value
        self.cond = threading.Condition()

    def wait(self) -> None:
        with self.cond:
            while self.value == 0:
                self.cond.wait()
            self.value -= 1

    def post(self) -> None:
        with self.cond:
            self.value += 1
            self.cond.notify()


if __name__ == "__main__":
    semaphore = Semaphore(2)
    peak = [0]
    active = [0]
    lock = threading.Lock()

    def worker() -> None:
        semaphore.wait()
        with lock:
            active[0] += 1
            peak[0] = max(peak[0], active[0])
        with lock:
            active[0] -= 1
        semaphore.post()

    threads = [threading.Thread(target=worker) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert peak[0] <= 2
    print("semaphore ok, peak:", peak[0])
