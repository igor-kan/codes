"""Alternating-bit stop-and-wait RDT over a lossy simulated channel."""
from dataclasses import dataclass
import random


@dataclass
class Channel:
    loss: float = 0.3
    seed: int = 0

    def __post_init__(self) -> None:
        self.rng = random.Random(self.seed)

    def transmit(self, packet) -> object | None:
        if self.rng.random() < self.loss:
            return None
        return packet


def checksum(data: str) -> int:
    return sum(map(ord, data)) % 256


def rdt_send(messages: list[str], channel: Channel) -> tuple[list[str], int]:
    seq = 0
    delivered = []
    transmissions = 0
    for message in messages:
        packet = {"seq": seq, "data": message, "sum": checksum(message)}
        while True:
            transmissions += 1
            acked = channel.transmit(packet)
            if acked and acked["sum"] == checksum(acked["data"]):
                delivered.append(acked["data"])
                seq ^= 1  # alternate bit
                break
    return delivered, transmissions


if __name__ == "__main__":
    channel = Channel(loss=0.0)
    delivered, transmissions = rdt_send(["a", "b", "c"], channel)
    assert delivered == ["a", "b", "c"] and transmissions == 3
    print("rdt stop-and-wait ok")
