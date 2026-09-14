"""Stop-and-wait reliable transfer simulation with loss and corruption."""
import random
from dataclasses import dataclass


@dataclass
class Packet:
    seq: int
    payload: str
    checksum: int


def checksum(text: str) -> int:
    return sum(map(ord, text)) % 256


class Channel:
    def __init__(self, loss: float = 0.2, corrupt: float = 0.1, seed: int = 0) -> None:
        self.rng = random.Random(seed)
        self.loss = loss
        self.corrupt = corrupt
        self.transmissions = 0

    def transmit(self, packet: Packet) -> Packet | None:
        self.transmissions += 1
        if self.rng.random() < self.loss:
            return None
        if self.rng.random() < self.corrupt:
            return Packet(packet.seq, "corrupted", 0)
        return packet


def rdt_send(channel: Channel, messages: list[str]) -> int:
    delivered = 0
    for seq, message in enumerate(messages):
        packet = Packet(seq, message, checksum(message))
        while True:
            echoed = channel.transmit(packet)
            if echoed and echoed.checksum == checksum(echoed.payload):
                delivered += 1
                break
    return delivered


if __name__ == "__main__":
    channel = Channel(loss=0.0, corrupt=0.0)
    assert rdt_send(channel, ["a", "b", "c"]) == 3
    print("transmissions:", channel.transmissions)
