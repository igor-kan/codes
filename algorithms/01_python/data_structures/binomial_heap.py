"""Binomial heap with merge, insert and extract-min."""
class Node:
    __slots__ = ("key", "degree", "parent", "child", "sibling")

    def __init__(self, key: int) -> None:
        self.key, self.degree = key, 0
        self.parent = self.child = self.sibling = None


class BinomialHeap:
    def __init__(self) -> None:
        self.head: Node | None = None

    @staticmethod
    def _merge_roots(a: Node | None, b: Node | None) -> Node | None:
        if not a:
            return b
        if not b:
            return a
        if a.degree <= b.degree:
            a.sibling = BinomialHeap._merge_roots(a.sibling, b)
            return a
        b.sibling = BinomialHeap._merge_roots(a, b.sibling)
        return b

    def union(self, other: "BinomialHeap") -> "BinomialHeap":
        result = BinomialHeap()
        result.head = self._merge_roots(self.head, other.head)
        if result.head is None:
            return result
        prev, curr, nxt = None, result.head, result.head.sibling
        while nxt:
            if curr.degree != nxt.degree or (nxt.sibling and nxt.sibling.degree == curr.degree):
                prev, curr, nxt = curr, nxt, nxt.sibling
            elif curr.key <= nxt.key:
                curr.sibling = nxt.sibling
                nxt.parent = curr
                nxt.sibling = curr.child
                curr.child = nxt
                curr.degree += 1
                nxt = curr.sibling
            else:
                if prev:
                    prev.sibling = nxt
                else:
                    result.head = nxt
                curr.parent = nxt
                curr.sibling = nxt.child
                nxt.child = curr
                nxt.degree += 1
                curr, nxt = nxt, nxt.sibling
        return result

    def insert(self, key: int) -> None:
        self.head = self.union(_singleton(key)).head

    def extract_min(self) -> int:
        if not self.head:
            raise IndexError("empty heap")
        best, best_prev, prev, node = self.head, None, None, self.head
        while node:
            if best is None or node.key < best.key:
                best, best_prev = node, prev
            prev, node = node, node.sibling
        if best_prev:
            best_prev.sibling = best.sibling
        else:
            self.head = best.sibling
        child = best.child
        reversed_children = None
        while child:
            nxt = child.sibling
            child.sibling = reversed_children
            child.parent = None
            reversed_children = child
            child = nxt
        other = BinomialHeap()
        other.head = reversed_children
        self.head = self.union(other).head
        return best.key


def _singleton(key: int) -> "BinomialHeap":
    heap = BinomialHeap()
    heap.head = Node(key)
    return heap


if __name__ == "__main__":
    heap = BinomialHeap()
    for key in [10, 20, 5, 30, 1]:
        heap.insert(key)
    assert heap.extract_min() == 1
    assert heap.extract_min() == 5
    print("binomial heap ok")
