"""Producer/consumer with condition variables and a bounded buffer."""
import threading
from collections import deque


class BoundedBuffer:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.buffer: deque[int] = deque()
        self.cond = threading.Condition()

    def put(self, item: int) -> None:
        with self.cond:
            while len(self.buffer) == self.capacity:
                self.cond.wait()
            self.buffer.append(item)
            self.cond.notify_all()

    def get(self) -> int:
        with self.cond:
            while not self.buffer:
                self.cond.wait()
            item = self.buffer.popleft()
            self.cond.notify_all()
            return item


if __name__ == "__main__":
    buffer = BoundedBuffer(3)
    items = list(range(20))
    consumed: list[int] = []

    def producer() -> None:
        for item in items:
            buffer.put(item)

    def consumer() -> None:
        for _ in items:
            consumed.append(buffer.get())

    threads = [threading.Thread(target=producer), threading.Thread(target=consumer)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert sorted(consumed) == items
    print("producer/consumer ok")
