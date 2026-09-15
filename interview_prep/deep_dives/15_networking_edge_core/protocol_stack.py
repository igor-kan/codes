"""Encapsulation and decapsulation through a layered stack."""
from dataclasses import dataclass, field


@dataclass
class Packet:
    payload: bytes
    headers: list[tuple[str, bytes]] = field(default_factory=list)

    def encapsulate(self, layer: str, header: bytes) -> "Packet":
        return Packet(self.payload, [(layer, header), *self.headers])

    def decapsulate(self) -> tuple[str, bytes, "Packet"]:
        (layer, header), rest = self.headers[0], self.headers[1:]
        return layer, header, Packet(self.payload, rest)

    def render(self) -> str:
        return " > ".join(f"{layer}({header.decode()})" for layer, header in self.headers)


if __name__ == "__main__":
    packet = Packet(b"GET /")
    packet = packet.encapsulate("tcp", b"80")
    packet = packet.encapsulate("ip", b"10.0.0.1")
    packet = packet.encapsulate("eth", b"aa:bb")
    assert packet.render() == "eth(aa:bb) > ip(10.0.0.1) > tcp(80)"
    layer, header, inner = packet.decapsulate()
    assert layer == "eth" and header == b"aa:bb"
    print("protocol stack ok")
