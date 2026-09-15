"""MCS queue lock: each waiter spins on its own node (scalable)."""
import threading
from dataclasses import dataclass, field


@dataclass
class Node:
    locked: bool = False
    next_node: "Node | None" = None


class MCSLock:
    def __init__(self) -> None:
        self.tail: Node | None = None
        self._guard = threading.Lock()

    def lock(self, node: Node) -> None:
        with self._guard:
            predecessor = self.tail
            self.tail = node
        if predecessor is not None:
            predecessor.next_node = node
            node.locked = False
            while not node.locked:
                pass

    def unlock(self, node: Node) -> None:
        with self._guard:
            if node.next_node is None:
                if self.tail is node:
                    self.tail = None
                    return
                while node.next_node is None:
                    pass
            node.next_node.locked = True
            node.next_node = None


# The toy MCS above requires true parallelism to be meaningful; it is included
# for study. The test below exercises a single-threaded lock/unlock cycle.
if __name__ == "__main__":
    lock = MCSLock()
    node = Node()
    lock.lock(node)
    lock.unlock(node)
    print("mcs queue lock ok")
