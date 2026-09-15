"""Output-port scheduling: FIFO, priority and weighted fair queueing."""
from dataclasses import dataclass, field
import itertools


@dataclass
class Packet:
    flow: str
    size: int


class FIFO:
    def __init__(self) -> None:
        self.queue: list[Packet] = []

    def enqueue(self, packet: Packet) -> None:
        self.queue.append(packet)

    def dequeue(self) -> Packet | None:
        return self.queue.pop(0) if self.queue else None


class PriorityQueueing:
    def __init__(self, classes: list[str]) -> None:
        self.queues = {name: [] for name in classes}
        self.order = classes

    def enqueue(self, packet: Packet) -> None:
        self.queues[packet.flow].append(packet)

    def dequeue(self) -> Packet | None:
        for name in self.order:
            if self.queues[name]:
                return self.queues[name].pop(0)
        return None


class WeightedFairQueueing:
    def __init__(self, weights: dict[str, int]) -> None:
        self.weights = weights
        self.virtual_time = {flow: 0 for flow in weights}
        self.queues: dict[str, list[Packet]] = {flow: [] for flow in weights}
        self.rr = itertools.cycle(weights)

    def enqueue(self, packet: Packet) -> None:
        self.queues[packet.flow].append(packet)
        self.virtual_time[packet.flow] += packet.size / self.weights[packet.flow]

    def dequeue(self) -> Packet | None:
        available = [f for f in self.queues if self.queues[f]]
        if not available:
            return None
        chosen = min(available, key=lambda f: self.virtual_time[f])
        return self.queues[chosen].pop(0)


if __name__ == "__main__":
    fifo = FIFO()
    fifo.enqueue(Packet("a", 100))
    fifo.enqueue(Packet("b", 100))
    assert fifo.dequeue().flow == "a"

    pq = PriorityQueueing(["voice", "bulk"])
    pq.enqueue(Packet("bulk", 1500))
    pq.enqueue(Packet("voice", 64))
    assert pq.dequeue().flow == "voice"
    print("scheduling ok")
