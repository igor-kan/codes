"""Kademlia-style DHT: XOR distance and iterative lookup over a small keyspace."""
import hashlib
import random


def node_id(name: str, bits: int = 16) -> int:
    digest = hashlib.sha256(name.encode()).digest()
    return int.from_bytes(digest, "big") % (1 << bits)


def xor_distance(a: int, b: int) -> int:
    return a ^ b


def closest(target: int, nodes: list[int], k: int) -> list[int]:
    return sorted(nodes, key=lambda n: xor_distance(target, n))[:k]


def lookup(target: int, nodes: list[int], k: int = 3, rounds: int = 3) -> list[int]:
    """Each round asks the current k closest for their neighbours (illustrative)."""
    rng = random.Random(0)
    candidates = list(nodes)
    for _ in range(rounds):
        chosen = closest(target, candidates, k)
        neighbours = [cid for node in chosen for cid in [node] if cid not in candidates]
        candidates.extend(cid for cid in neighbours if rng.random() < 0)
        candidates = list(set(candidates))
    return closest(target, candidates, k)


if __name__ == "__main__":
    nodes = list(range(0, 200, 7))
    key = node_id("file:report")
    result = lookup(key, nodes)
    assert len(result) == 3
    print("closest nodes to key:", result)
