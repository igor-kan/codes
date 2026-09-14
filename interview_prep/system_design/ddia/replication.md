# Replication (DDIA Ch. 5)

Keep copies of data on multiple nodes for availability, latency and read scale.

## Single-leader

- All writes to the leader; followers apply the log.
- **Synchronous** replication is durable but blocks on slow followers;
  **asynchronous** risks data loss on failover.
- Failover hazards: split brain, lost writes, stale reads.

## Multi-leader

- Multiple nodes accept writes; conflicts resolved by last-write-wins, version
  vectors, or application-specific merge (CRDTs).
- Common across regions and in offline-capable clients.

## Leaderless

- Quorums: `W + R > N` gives overlap and read-your-writes.
- Anti-entropy (read repair, hinted handoff) reconciles replicas.

## Replication log formats

Statement-based, WAL shipping, logical (row-based), trigger-based.
