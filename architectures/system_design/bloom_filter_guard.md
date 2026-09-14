# Bloom Filter Guard

Use a Bloom filter — a compact probabilistic set with no false negatives — to
avoid expensive lookups for keys that definitely do not exist.

```python
from hashlib import sha256

class BloomFilter:
    def __init__(self, bits: int, hashes: int) -> None:
        self.bits = bytearray(bits // 8 + 1)
        self.hashes = hashes
        self.size = bits

    def _positions(self, key: str):
        digest = sha256(key.encode()).digest()
        for i in range(self.hashes):
            yield int.from_bytes(digest[i * 2:i * 2 + 2], "big") % self.size

    def add(self, key: str) -> None:
        for pos in self._positions(key):
            self.bits[pos // 8] |= 1 << (pos % 8)

    def maybe_contains(self, key: str) -> bool:
        return all(self.bits[p // 8] & (1 << (p % 8)) for p in self._positions(key))
```

## Use cases

- Cache penetration protection: check the filter before hitting the database.
- Deduplicating crawl URLs or event IDs at scale.
- Avoiding disk seeks in LSM-tree storage engines (e.g. RocksDB, Cassandra).

**Trade-off:** false positives cause unnecessary cache misses or lookups, so
size the filter for the target false-positive rate and monitor saturation.

Related: Caching (Cache-Aside), Sharding, Probabilistic Data Structures.
