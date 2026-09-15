"""NAT translation table simulation."""
from dataclasses import dataclass, field


@dataclass
class NatTable:
    public_ip: str
    next_port: int = 40000
    translations: dict[tuple[str, int], tuple[str, int]] = field(default_factory=dict)
    reverse: dict[tuple[str, int], tuple[str, int]] = field(default_factory=dict)

    def outbound(self, private_ip: str, private_port: int) -> tuple[str, int]:
        key = (private_ip, private_port)
        if key not in self.translations:
            self.translations[key] = (self.public_ip, self.next_port)
            self.reverse[(self.public_ip, self.next_port)] = key
            self.next_port += 1
        return self.translations[key]

    def inbound(self, public_port: int) -> tuple[str, int] | None:
        return self.reverse.get((self.public_ip, public_port))


if __name__ == "__main__":
    nat = NatTable(public_ip="203.0.113.1")
    assert nat.outbound("10.0.0.2", 5000) == ("203.0.113.1", 40000)
    assert nat.inbound(40000) == ("10.0.0.2", 5000)
    print("nat ok")
