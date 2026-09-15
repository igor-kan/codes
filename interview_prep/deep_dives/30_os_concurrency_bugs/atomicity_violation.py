"""Atomicity violation: check-then-act races."""
import threading


class BrokenStack:
    def __init__(self) -> None:
        self.items: list[int] = []
        self.lock = threading.Lock()

    def push(self, value: int) -> None:
        with self.lock:
            self.items.append(value)

    def pop(self) -> int | None:
        if not self.items:          # check
            return None
        return self.items.pop()     # act (not atomic with the check)


class FixedStack:
    def __init__(self) -> None:
        self.items: list[int] = []
        self.lock = threading.Lock()

    def push(self, value: int) -> None:
        with self.lock:
            self.items.append(value)

    def pop(self) -> int | None:
        with self.lock:             # check and act under one lock
            if not self.items:
                return None
            return self.items.pop()


if __name__ == "__main__":
    stack = FixedStack()
    for i in range(10):
        stack.push(i)
    assert stack.pop() == 9
    print("atomicity fixed with locking")
