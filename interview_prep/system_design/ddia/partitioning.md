# Partitioning (DDIA Ch. 6)

Distribute data across nodes so each holds a subset.

## Strategies

- **Key range:** ordered, efficient scans, hotspot on sequential keys.
- **Hash:** even spread, loses range queries.
- **Consistent hashing:** minimal movement when nodes change.

## Secondary indexes

- **By document (local):** each partition indexes its own docs; scatter/gather.
- **By term (global):** index partitioned separately; writes touch many nodes.

## Rebalancing

- Fixed number of partitions moved between nodes.
- Dynamic partition splitting based on size.
- Avoid hash `mod N`; prefer many partitions + mapping.

## Request routing

Coordination service (ZooKeeper/etcd), gossip protocol, or leader-routed.

## Hot spots

Salting keys, key partitioning, and workload-aware sharding.
