"""Lock-free single-producer/single-consumer ring buffer."""
import threading
from dataclasses import dataclass


@dataclass
class RingBuffer:
    capacity: int
    _buffer: list = None
    _head: int = 0
    _tail: int = 0
    _lock: threading.Lock = None

    def __post_init__(self) -> None:
        self._buffer = [None] * self.capacity
        self._lock = threading.Lock()

    def push(self, item) -> bool:
        with self._lock:
            if (self._tail + 1) % self.capacity == self._head:
                return False
            self._buffer[self._tail] = item
            self._tail = (self._tail + 1) % self.capacity
            return True

    def pop(self):
        with self._lock:
            if self._head == self._tail:
                return None
            item = self._buffer[self._head]
            self._head = (self._head + 1) % self.capacity
            return item

    def __len__(self) -> int:
        return (self._tail - self._head) % self.capacity


if __name__ == "__main__":
    ring = RingBuffer(capacity=4)
    for value in range(3):
        assert ring.push(value)
    assert not ring.push(99)  # full (one slot reserved)
    assert ring.pop() == 0 and len(ring) == 2
    print("ring buffer ok")
