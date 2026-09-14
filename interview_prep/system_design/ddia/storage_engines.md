# Storage Engines (DDIA Ch. 3)

## LSM trees

- Writes go to an in-memory memtable and a commit log.
- Flush to immutable SSTables; background compaction merges them.
- Great write throughput; read amplification from checking multiple levels;
  Bloom filters reduce lookups.
- Used by LevelDB, RocksDB, Cassandra, ScyllaDB, HBase.

## B-trees

- Fixed-size pages updated in place; rebalancing on splits and merges.
- Predictable read latency; write amplification from page writes.
- Used by PostgreSQL, MySQL InnoDB, SQLite, SQL Server.

## Other structures

- Hash indexes (point lookups only).
- Column-oriented storage for analytics (compression, vectorized scans).
- In-memory and persistent-memory engines.
- Graph and full-text indexes.

## Metrics

Write/read amplification, space amplification, and tail latency.
