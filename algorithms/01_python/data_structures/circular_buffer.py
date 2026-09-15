"""Fixed-size circular buffer."""
class CircularBuffer:
    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.buffer = [None] * capacity
        self.capacity = capacity
        self.size = 0
        self.head = 0

    def push(self, value) -> None:
        self.buffer[(self.head + self.size) % self.capacity] = value
        if self.size < self.capacity:
            self.size += 1
        else:
            self.head = (self.head + 1) % self.capacity

    def pop(self):
        if self.size == 0:
            raise IndexError("empty buffer")
        value = self.buffer[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return value

    def __iter__(self):
        for i in range(self.size):
            yield self.buffer[(self.head + i) % self.capacity]


if __name__ == "__main__":
    buffer = CircularBuffer(3)
    for value in [1, 2, 3, 4]:
        buffer.push(value)
    assert list(buffer) == [2, 3, 4]
    assert buffer.pop() == 2
    print("circular buffer ok")
