"""Longest-prefix match with a binary trie."""
from dataclasses import dataclass, field


@dataclass
class TrieNode:
    children: dict[int, "TrieNode"] = field(default_factory=dict)
    next_hop: str | None = None


def ip_to_int(address: str) -> int:
    return int.from_bytes(bytes(int(x) for x in address.split(".")), "big")


def insert(root: TrieNode, prefix: str, next_hop: str) -> None:
    network, length = prefix.split("/")
    node = root
    for i in range(int(length)):
        bit = (ip_to_int(network) >> (31 - i)) & 1
        node = node.children.setdefault(bit, TrieNode())
    node.next_hop = next_hop


def lookup(root: TrieNode, address: str) -> str | None:
    node = root
    best = node.next_hop
    bits = ip_to_int(address)
    for i in range(32):
        node = node.children.get((bits >> (31 - i)) & 1)
        if node is None:
            break
        if node.next_hop is not None:
            best = node.next_hop
    return best


if __name__ == "__main__":
    root = TrieNode()
    insert(root, "10.0.0.0/8", "A")
    insert(root, "10.0.16.0/20", "B")
    insert(root, "0.0.0.0/0", "default")
    assert lookup(root, "10.0.16.5") == "B"
    assert lookup(root, "10.1.0.1") == "A"
    assert lookup(root, "8.8.8.8") == "default"
    print("longest prefix match ok")
