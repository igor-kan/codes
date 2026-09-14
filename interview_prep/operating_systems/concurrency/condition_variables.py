"""Condition variables: wait with a predicate to avoid lost wakeups."""
import threading


class BoundedBuffer:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.buffer: list[int] = []
        self.mutex = threading.Lock()
        self.not_full = threading.Condition(self.mutex)
        self.not_empty = threading.Condition(self.mutex)

    def put(self, item: int) -> None:
        with self.mutex:
            while len(self.buffer) == self.capacity:
                self.not_full.wait()
            self.buffer.append(item)
            self.not_empty.notify()

    def get(self) -> int:
        with self.mutex:
            while not self.buffer:
                self.not_empty.wait()
            item = self.buffer.pop(0)
            self.not_full.notify()
            return item


if __name__ == "__main__":
    buffer = BoundedBuffer(2)
    produced = list(range(10))
    consumed: list[int] = []

    def producer() -> None:
        for item in produced:
            buffer.put(item)

    def consumer() -> None:
        for _ in produced:
            consumed.append(buffer.get())

    threads = [threading.Thread(target=producer), threading.Thread(target=consumer)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert sorted(consumed) == produced
    print("bounded buffer ok")
