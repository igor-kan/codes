# Peer-to-Peer (P2P)

Peers exchange resources directly, scaling with participants instead of a
central server.

## Architectures

- **Centralized directory** (Napster): index server, direct transfers.
- **Decentralized flooding** (Gnutella): query floods the overlay.
- **Structured DHT** (BitTorrent, Kademlia): keys map to responsible peers.

## BitTorrent

- Content split into pieces; a `.torrent` has piece hashes and trackers.
- Peers exchange **choke/unchoke**, **interested**, and **have** messages.
- **Tit-for-tat** incentivizes uploads; rarest-first improves availability.

## DHTs

- Consistent hashing on node IDs; lookups in `O(log n)` hops.
- Redundancy places replicas on nearby IDs.
- NAT traversal via STUN/TURN or hole punching.

## Trade-offs

Resilience and scale vs. abuse, inconsistent availability, and legal/IP concerns.
