"""Fibonacci heap (insert and extract-min; decrease-key noted)."""
import math


class Node:
    __slots__ = ("key", "degree", "marked", "parent", "child", "left", "right")

    def __init__(self, key: int) -> None:
        self.key, self.degree, self.marked = key, 0, False
        self.parent = self.child = None
        self.left = self.right = self


class FibonacciHeap:
    def __init__(self) -> None:
        self.min: Node | None = None
        self.count = 0

    def insert(self, key: int) -> Node:
        node = Node(key)
        if self.min is None:
            self.min = node
        else:
            self._link_siblings(self.min, node)
            if key < self.min.key:
                self.min = node
        self.count += 1
        return node

    @staticmethod
    def _link_siblings(a: Node, b: Node) -> None:
        a.right.left = b
        b.right = a.right
        a.right = b
        b.left = a

    def extract_min(self) -> int:
        min_node = self.min
        if min_node is None:
            raise IndexError("empty heap")
        if min_node.child:
            children = [min_node.child]
            child = min_node.child.right
            while child is not min_node.child:
                children.append(child)
                child = child.right
            for child in children:
                self._link_siblings(min_node, child)
                child.parent = None
        min_node.right.left = min_node.left
        min_node.left.right = min_node.right
        if min_node is min_node.right:
            self.min = None
        else:
            self.min = min_node.right
            self._consolidate()
        self.count -= 1
        return min_node.key

    def _consolidate(self) -> None:
        max_degree = int(math.log2(max(1, self.count))) + 2
        table: list[Node | None] = [None] * max_degree
        nodes = []
        start = self.min
        nodes.append(start)
        node = start.right
        while node is not start:
            nodes.append(node)
            node = node.right
        for current in nodes:
            degree = current.degree
            while table[degree]:
                other = table[degree]
                if current.key > other.key:
                    current, other = other, current
                self._link(other, current)
                current.degree += 1
                table[degree] = None
                degree += 1
            table[degree] = current
        self.min = None
        for entry in table:
            if entry is not None:
                entry.left = entry.right = entry
                if self.min is None:
                    self.min = entry
                else:
                    self._link_siblings(self.min, entry)
                    if entry.key < self.min.key:
                        self.min = entry

    @staticmethod
    def _link(child: Node, parent: Node) -> None:
        child.left.right = child.right
        child.right.left = child.left
        child.parent = parent
        if parent.child is None:
            parent.child = child
            child.left = child.right = child
        else:
            FibonacciHeap._link_siblings(parent.child, child)


if __name__ == "__main__":
    heap = FibonacciHeap()
    for key in [9, 3, 7, 1, 5]:
        heap.insert(key)
    assert heap.extract_min() == 1
    print("fibonacci heap ok")
