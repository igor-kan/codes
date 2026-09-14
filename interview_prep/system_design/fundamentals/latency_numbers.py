"""Back-of-the-envelope latency numbers (Jeff Dean's classic table)."""
LATENCY_NS = {
    "L1 cache reference": 1,
    "L2 cache reference": 4,
    "main memory reference": 100,
    "mutex lock/unlock": 17,
    "compress 1KB": 2_000,
    "send 1KB over 1Gbps": 10_000,
    "read 4KB randomly from SSD": 150_000,
    "read 1MB sequentially from memory": 250_000,
    "round trip within datacenter": 500_000,
    "read 1MB sequentially from SSD": 1_000_000,
    "disk seek": 10_000_000,
    "read 1MB sequentially from disk": 20_000_000,
    "round trip CA<->Netherlands": 150_000_000,
}


def humanise(ns: int) -> str:
    for unit, scale in (("s", 1e9), ("ms", 1e6), ("us", 1e3), ("ns", 1)):
        if ns >= scale:
            return f"{ns / scale:.2f} {unit}"
    return f"{ns} ns"


if __name__ == "__main__":
    assert LATENCY_NS["L1 cache reference"] == 1
    assert humanise(100_000_000).endswith("ms")
    for name, ns in list(LATENCY_NS.items())[:3]:
        print(f"{name}: {humanise(ns)}")
