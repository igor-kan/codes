"""CIDR matching and next-hop resolution for a small forwarding table."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Route:
    network: str
    prefix_len: int
    next_hop: str

    def matches(self, address: str) -> bool:
        network_int = int.from_bytes(bytes(int(x) for x in self.network.split(".")), "big")
        address_int = int.from_bytes(bytes(int(x) for x in address.split(".")), "big")
        mask = (0xFFFFFFFF << (32 - self.prefix_len)) & 0xFFFFFFFF if self.prefix_len else 0
        return (network_int & mask) == (address_int & mask)


def forward(routes: list[Route], address: str) -> str:
    candidates = [r for r in routes if r.matches(address)]
    if not candidates:
        return "drop"
    best = max(candidates, key=lambda r: r.prefix_len)
    return best.next_hop


if __name__ == "__main__":
    routes = [
        Route("192.168.0.0", 16, "lan"),
        Route("192.168.1.0", 24, "vlan1"),
        Route("0.0.0.0", 0, "internet"),
    ]
    assert forward(routes, "192.168.1.10") == "vlan1"
    assert forward(routes, "192.168.2.10") == "lan"
    assert forward(routes, "8.8.8.8") == "internet"
    print("router lookup ok")
