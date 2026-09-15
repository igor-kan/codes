"""Binary max-heap."""


class MaxHeap:
    def __init__(self) -> None:
        self.data: list[int] = []

    def __len__(self) -> int:
        return len(self.data)

    def push(self, value: int) -> None:
        self.data.append(value)
        i = len(self.data) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.data[parent] >= self.data[i]:
                break
            self.data[parent], self.data[i] = self.data[i], self.data[parent]
            i = parent

    def pop(self) -> int:
        top = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            i = 0
            while True:
                left, right = 2 * i + 1, 2 * i + 2
                best = i
                if left < len(self.data) and self.data[left] > self.data[best]:
                    best = left
                if right < len(self.data) and self.data[right] > self.data[best]:
                    best = right
                if best == i:
                    break
                self.data[i], self.data[best] = self.data[best], self.data[i]
                i = best
        return top


if __name__ == "__main__":
    heap = MaxHeap()
    for value in [5, 3, 8, 1, 4]:
        heap.push(value)
    ordered = [heap.pop() for _ in range(len(heap))]
    assert ordered == sorted([5, 3, 8, 1, 4], reverse=True)
    print("max heap ok")
