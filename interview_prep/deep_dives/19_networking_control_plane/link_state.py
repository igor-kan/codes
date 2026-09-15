"""Link-state flooding and topology graph construction."""
from dataclasses import dataclass, field


@dataclass
class LinkStatePacket:
    origin: str
    sequence: int
    neighbors: dict[str, int]


class LinkStateDatabase:
    def __init__(self) -> None:
        self.lsdb: dict[str, LinkStatePacket] = {}

    def receive(self, packet: LinkStatePacket) -> bool:
        current = self.lsdb.get(packet.origin)
        if current is None or packet.sequence > current.sequence:
            self.lsdb[packet.origin] = packet
            return True
        return False

    def graph(self) -> dict[str, dict[str, int]]:
        return {origin: dict(packet.neighbors) for origin, packet in self.lsdb.items()}


if __name__ == "__main__":
    db = LinkStateDatabase()
    assert db.receive(LinkStatePacket("A", 1, {"B": 1}))
    assert not db.receive(LinkStatePacket("A", 1, {"B": 9}))  # stale sequence
    assert db.receive(LinkStatePacket("B", 2, {"A": 1, "C": 1}))
    assert set(db.graph()) == {"A", "B"}
    print("link-state database ok")
