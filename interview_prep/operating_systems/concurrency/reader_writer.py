"""Reader/writer lock favoring writers (no starvation)."""
import threading


class ReadWriteLock:
    def __init__(self) -> None:
        self.mutex = threading.Lock()
        self.readers = 0
        self.writer = False
        self.can_read = threading.Condition(self.mutex)
        self.can_write = threading.Condition(self.mutex)

    def acquire_read(self) -> None:
        with self.mutex:
            while self.writer:
                self.can_read.wait()
            self.readers += 1

    def release_read(self) -> None:
        with self.mutex:
            self.readers -= 1
            if self.readers == 0:
                self.can_write.notify()

    def acquire_write(self) -> None:
        with self.mutex:
            while self.writer or self.readers > 0:
                self.can_write.wait()
            self.writer = True

    def release_write(self) -> None:
        with self.mutex:
            self.writer = False
            self.can_read.notify_all()
            self.can_write.notify()


if __name__ == "__main__":
    rwlock = ReadWriteLock()
    shared = {"value": 0}

    def reader() -> None:
        rwlock.acquire_read()
        assert shared["value"] >= 0
        rwlock.release_read()

    def writer() -> None:
        rwlock.acquire_write()
        shared["value"] += 1
        rwlock.release_write()

    threads = [threading.Thread(target=writer) for _ in range(5)]
    threads += [threading.Thread(target=reader) for _ in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert shared["value"] == 5
    print("reader/writer ok")
