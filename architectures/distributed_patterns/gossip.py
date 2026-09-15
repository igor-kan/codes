"""Gossip protocol: epidemic dissemination of state."""
import random
from dataclasses import dataclass, field


@dataclass
class GossipNode:
    name: str
    value: int = 0
    clock: int = 0
    peers: list[str] = field(default_factory=list)


def disseminate(nodes: dict[str, GossipNode], rounds: int = 10, seed: int = 0) -> None:
    rng = random.Random(seed)
    for _ in range(rounds):
        for node in nodes.values():
            peer = nodes[rng.choice(node.peers)]
            if node.clock > peer.clock:
                peer.value, peer.clock = node.value, node.clock
            elif peer.clock > node.clock:
                node.value, node.clock = peer.value, peer.clock


if __name__ == "__main__":
    nodes = {name: GossipNode(name, peers=["a", "b", "c"]) for name in "abc"}
    nodes["a"].value, nodes["a"].clock = 42, 1
    disseminate(nodes)
    assert all(node.value == 42 for node in nodes.values())
    print("gossip ok")
