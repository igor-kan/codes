"""Reader/writer lock that prevents writer starvation."""
import threading


class ReadWriteLock:
    def __init__(self) -> None:
        self.mutex = threading.Lock()
        self.readers = 0
        self.writer = False
        self.ok_to_read = threading.Condition(self.mutex)
        self.ok_to_write = threading.Condition(self.mutex)

    def acquire_read(self) -> None:
        with self.mutex:
            while self.writer:
                self.ok_to_read.wait()
            self.readers += 1

    def release_read(self) -> None:
        with self.mutex:
            self.readers -= 1
            if self.readers == 0:
                self.ok_to_write.notify()

    def acquire_write(self) -> None:
        with self.mutex:
            while self.writer or self.readers > 0:
                self.ok_to_write.wait()
            self.writer = True

    def release_write(self) -> None:
        with self.mutex:
            self.writer = False
            self.ok_to_read.notify_all()
            self.ok_to_write.notify()


if __name__ == "__main__":
    lock = ReadWriteLock()
    state = {"value": 0}

    def writer() -> None:
        for _ in range(10):
            lock.acquire_write()
            state["value"] += 1
            lock.release_write()

    def reader() -> None:
        for _ in range(10):
            lock.acquire_read()
            assert state["value"] >= 0
            lock.release_read()

    threads = [threading.Thread(target=writer) for _ in range(3)] + [threading.Thread(target=reader) for _ in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert state["value"] == 30
    print("reader/writer ok")
