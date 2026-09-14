"""ARP cache simulation: map IP addresses to MAC addresses."""
from dataclasses import dataclass, field


@dataclass
class ArpCache:
    entries: dict[str, str] = field(default_factory=dict)

    def learn(self, ip: str, mac: str) -> None:
        self.entries[ip] = mac

    def lookup(self, ip: str) -> str | None:
        return self.entries.get(ip)

    def resolve(self, ip: str, responders: dict[str, str]) -> str | None:
        mac = responders.get(ip)
        if mac:
            self.learn(ip, mac)
        return mac


if __name__ == "__main__":
    network = {"10.0.0.1": "aa:bb:cc:00:00:01", "10.0.0.2": "aa:bb:cc:00:00:02"}
    cache = ArpCache()
    assert cache.resolve("10.0.0.1", network) == "aa:bb:cc:00:00:01"
    assert cache.lookup("10.0.0.1") == "aa:bb:cc:00:00:01"
    print("arp cache ok")
