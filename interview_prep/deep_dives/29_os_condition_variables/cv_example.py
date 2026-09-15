"""Condition variables with predicates."""
import threading


class Box:
    def __init__(self) -> None:
        self.value = None
        self.cond = threading.Condition()

    def put(self, value: int) -> None:
        with self.cond:
            while self.value is not None:
                self.cond.wait()
            self.value = value
            self.cond.notify_all()

    def take(self) -> int:
        with self.cond:
            while self.value is None:
                self.cond.wait()
            value, self.value = self.value, None
            self.cond.notify_all()
            return value


if __name__ == "__main__":
    box = Box()

    def producer() -> None:
        for i in range(5):
            box.put(i)

    received = []
    threads = [threading.Thread(target=producer), threading.Thread(target=lambda: [received.append(box.take()) for _ in range(5)])]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert received == [0, 1, 2, 3, 4]
    print("condition variable ok")
