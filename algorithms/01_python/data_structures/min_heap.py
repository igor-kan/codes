"""Binary min-heap with build-heap and heapify."""
class MinHeap:
    def __init__(self, values: list[int] | None = None) -> None:
        self.data = list(values or [])
        for i in range(len(self.data) // 2 - 1, -1, -1):
            self._sift_down(i)

    def push(self, value: int) -> None:
        self.data.append(value)
        i = len(self.data) - 1
        while i > 0 and self.data[(i - 1) // 2] > self.data[i]:
            parent = (i - 1) // 2
            self.data[i], self.data[parent] = self.data[parent], self.data[i]
            i = parent

    def pop(self) -> int:
        if not self.data:
            raise IndexError("pop from empty heap")
        root = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self._sift_down(0)
        return root

    def _sift_down(self, i: int) -> None:
        n = len(self.data)
        while True:
            smallest, left, right = i, 2 * i + 1, 2 * i + 2
            if left < n and self.data[left] < self.data[smallest]:
                smallest = left
            if right < n and self.data[right] < self.data[smallest]:
                smallest = right
            if smallest == i:
                return
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            i = smallest


if __name__ == "__main__":
    heap = MinHeap([5, 3, 8, 1, 4])
    assert heap.pop() == 1
    heap.push(0)
    assert heap.pop() == 0
    assert [heap.pop() for _ in range(4)] == [3, 4, 5, 8]
    print("min heap ok")
