"""Consistent Hashing with Virtual Nodes (Ketama Algorithm).

Provides deterministic distributed partition routing with minimal key migration
upon cluster scaling.
"""

import bisect
import hashlib
from typing import Dict, List, Optional

class ConsistentHashRing:
    def __init__(self, replicas: int = 100):
        self.replicas = replicas
        self.ring: List[int] = []  # Sorted hash positions
        self.node_map: Dict[int, str] = {}  # hash position -> physical node
        self.nodes: set[str] = set()

    def _hash(self, key: str) -> int:
        # MD5 128-bit hash truncated to 32-bit integer
        return int(hashlib.md5(key.encode('utf-8')).hexdigest()[:8], 16)

    def add_node(self, node: str) -> None:
        self.nodes.add(node)
        for i in range(self.replicas):
            vnode_key = f"{node}#vnode{i}"
            h = self._hash(vnode_key)
            bisect.insort(self.ring, h)
            self.node_map[h] = node

    def remove_node(self, node: str) -> None:
        if node not in self.nodes:
            return
        self.nodes.remove(node)
        for i in range(self.replicas):
            vnode_key = f"{node}#vnode{i}"
            h = self._hash(vnode_key)
            idx = bisect.bisect_left(self.ring, h)
            if idx < len(self.ring) and self.ring[idx] == h:
                del self.ring[idx]
            self.node_map.pop(h, None)

    def get_node(self, key: str) -> Optional[str]:
        if not self.ring:
            return None
        h = self._hash(key)
        idx = bisect.bisect_right(self.ring, h)
        if idx == len(self.ring):
            idx = 0  # Wrap around the ring
        return self.node_map[self.ring[idx]]

if __name__ == "__main__":
    ring = ConsistentHashRing(replicas=150)
    for node in ["cache-node-1", "cache-node-2", "cache-node-3"]:
        ring.add_node(node)

    # Distribute 1,000 keys
    keys = [f"user_session_{i}" for i in range(1000)]
    initial_alloc = {k: ring.get_node(k) for k in keys}

    # Add a 4th node: only ~25% of keys should migrate
    ring.add_node("cache-node-4")
    new_alloc = {k: ring.get_node(k) for k in keys}

    migrated = sum(1 for k in keys if initial_alloc[k] != new_alloc[k])
    migration_ratio = migrated / len(keys)

    print(f"[Distributed Systems] Key migration ratio upon node addition: {migration_ratio*100:.1f}% (Expected ~25%)")
    assert 0.15 <= migration_ratio <= 0.35, f"Unexpected migration ratio: {migration_ratio}"
