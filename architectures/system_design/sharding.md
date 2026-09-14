# Sharding (Horizontal Partitioning)

Split a dataset across nodes so each holds a subset, enabling horizontal scale.

## Strategies

| Strategy | How | Pros | Cons |
|:---|:---|:---|:---|
| Range | key ranges per shard | efficient range scans | hotspots on sequential keys |
| Hash | `hash(key) % N` | even distribution | resharding moves most keys |
| Consistent hash | ring with virtual nodes | minimal movement on change | more complex |
| Directory | lookup service maps key → shard | flexible rebalancing | extra hop, SPOF |

## Considerations

- **Shard key choice** determines balance and query patterns; avoid monotonically
  increasing keys for range sharding.
- **Cross-shard queries** are expensive; model around the access path.
- **Resharding** should be online and idempotent; prefer consistent hashing.
- **Transactions** across shards require two-phase commit or sagas.

Related: Consistent Hashing, CAP Theorem, CQRS, Partitioning.
