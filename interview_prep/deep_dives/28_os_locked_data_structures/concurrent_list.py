"""A coarse-locked linked list."""
import threading
from dataclasses import dataclass, field


@dataclass
class Node:
    value: int
    next: "Node | None" = None


class ConcurrentList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.lock = threading.Lock()

    def insert(self, value: int) -> None:
        with self.lock:
            self.head = Node(value, self.head)

    def contains(self, value: int) -> bool:
        with self.lock:
            node = self.head
            while node:
                if node.value == value:
                    return True
                node = node.next
            return False

    def values(self) -> list[int]:
        with self.lock:
            result = []
            node = self.head
            while node:
                result.append(node.value)
                node = node.next
            return result


if __name__ == "__main__":
    lst = ConcurrentList()
    threads = [threading.Thread(target=lst.insert, args=(i,)) for i in range(100)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert sorted(lst.values()) == list(range(100))
    print("concurrent list ok")
