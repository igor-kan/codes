"""A two-lock queue (separate head and tail locks)."""
import threading
from dataclasses import dataclass


@dataclass
class Node:
    value: int | None
    next: "Node | None" = None


class TwoLockQueue:
    def __init__(self) -> None:
        self.dummy = Node(None)
        self.head = self.dummy
        self.tail = self.dummy
        self.head_lock = threading.Lock()
        self.tail_lock = threading.Lock()

    def enqueue(self, value: int) -> None:
        node = Node(value)
        with self.tail_lock:
            self.tail.next = node
            self.tail = node

    def dequeue(self) -> int | None:
        with self.head_lock:
            if self.head.next is None:
                return None
            node = self.head.next
            self.head = node
            return node.value


if __name__ == "__main__":
    queue = TwoLockQueue()
    for i in range(5):
        queue.enqueue(i)
    assert [queue.dequeue() for _ in range(5)] == [0, 1, 2, 3, 4]
    assert queue.dequeue() is None
    print("two-lock queue ok")
