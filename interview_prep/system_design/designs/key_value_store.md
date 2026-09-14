# Design: Distributed Key-Value Store

## Requirements

- `get(key)`, `put(key, value)`, `delete(key)` with tunable consistency.
- Horizontally scalable, always available, low latency.

## Partitioning

- Consistent hashing with virtual nodes for even load.
- Replication factor N; primary plus N-1 replicas on the ring.

## Consistency

- Quorums: `W + R > N` gives strong-ish reads.
- Versioning with vector clocks or last-write-wins.
- Read repair and hinted handoff for anti-entropy.

## Storage engine

- LSM tree (RocksDB-style): memtable + SSTables + compaction.
- Memtable durability via WAL; Bloom filters per SSTable.

## Failure handling

- Gossip membership, hinted handoff for failed replicas.
- Merkle-tree anti-entropy to reconcile divergent ranges.
- Fencing tokens for stale leaders.

## Examples

DynamoDB, Cassandra, Riak, etcd (linearizable, Raft).
