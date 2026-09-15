"""Backpressure: bound a queue and reject/slow producers when full."""
import queue


class BoundedPipe:
    def __init__(self, capacity: int) -> None:
        self.queue: queue.Queue = queue.Queue(maxsize=capacity)
        self.rejected = 0

    def push(self, item: int) -> bool:
        try:
            self.queue.put_nowait(item)
            return True
        except queue.Full:
            self.rejected += 1
            return False

    def pop(self) -> int:
        return self.queue.get_nowait()


if __name__ == "__main__":
    pipe = BoundedPipe(capacity=2)
    assert pipe.push(1) and pipe.push(2)
    assert not pipe.push(3) and pipe.rejected == 1
    assert pipe.pop() == 1
    assert pipe.push(3)
    print("backpressure ok")
