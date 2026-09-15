"""Single-lock bounded buffer using two condition variables."""
import threading
from collections import deque


class BoundedBuffer:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.buffer: deque[int] = deque()
        self.mutex = threading.Lock()
        self.not_full = threading.Condition(self.mutex)
        self.not_empty = threading.Condition(self.mutex)

    def put(self, item: int) -> None:
        with self.not_full:
            while len(self.buffer) == self.capacity:
                self.not_full.wait()
            self.buffer.append(item)
            self.not_empty.notify()

    def get(self) -> int:
        with self.not_empty:
            while not self.buffer:
                self.not_empty.wait()
            item = self.buffer.popleft()
            self.not_full.notify()
            return item


if __name__ == "__main__":
    buffer = BoundedBuffer(2)
    buffer.put(1)
    buffer.put(2)
    assert buffer.get() == 1
    print("bounded buffer ok")
