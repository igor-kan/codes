"""Fine-grained list locking with a per-node mutex (hand-over-hand)."""
import threading
from dataclasses import dataclass, field


@dataclass
class Node:
    value: int
    lock: threading.Lock = field(default_factory=threading.Lock)
    next: "Node | None" = None


class FineGrainedList:
    def __init__(self) -> None:
        self.head = Node(float("-inf"))
        self.head.next = Node(float("inf"))

    def insert(self, value: int) -> None:
        prev = self.head
        prev.lock.acquire()
        cur = prev.next
        cur.lock.acquire()
        while cur.value < value:
            prev.lock.release()
            prev = cur
            cur = cur.next
            cur.lock.acquire()
        if cur.value != value:
            node = Node(value)
            node.next = cur
            prev.next = node
        cur.lock.release()
        prev.lock.release()

    def contains(self, value: int) -> bool:
        prev = self.head
        prev.lock.acquire()
        cur = prev.next
        cur.lock.acquire()
        while cur.value < value:
            prev.lock.release()
            prev = cur
            cur = cur.next
            cur.lock.acquire()
        found = cur.value == value
        cur.lock.release()
        prev.lock.release()
        return found


if __name__ == "__main__":
    lst = FineGrainedList()
    for value in [3, 1, 2, 5, 4]:
        lst.insert(value)
    assert lst.contains(4) and not lst.contains(9)
    print("fine-grained list ok")
