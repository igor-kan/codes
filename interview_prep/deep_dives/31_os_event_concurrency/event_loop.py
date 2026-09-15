"""A deterministic event loop with timers and callbacks."""
import heapq
from dataclasses import dataclass, field


@dataclass(order=True)
class Timer:
    when: int
    callback: object = field(compare=False)


class EventLoop:
    def __init__(self) -> None:
        self.time = 0
        self.timers: list[Timer] = []
        self.callbacks: list[object] = []

    def call_soon(self, callback) -> None:
        self.callbacks.append(callback)

    def call_later(self, delay: int, callback) -> None:
        heapq.heappush(self.timers, Timer(self.time + delay, callback))

    def run(self, until: int) -> None:
        while self.time <= until:
            while self.callbacks:
                self.callbacks.pop(0)()
            if self.timers and self.timers[0].when <= self.time:
                heapq.heappop(self.timers).callback()
            self.time += 1


if __name__ == "__main__":
    loop = EventLoop()
    order: list[str] = []
    loop.call_soon(lambda: order.append("immediate"))
    loop.call_later(3, lambda: order.append("later"))
    loop.call_later(1, lambda: order.append("soon"))
    loop.run(5)
    assert order == ["immediate", "soon", "later"]
    print("event loop ok:", order)
