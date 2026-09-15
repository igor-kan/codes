# Design: Distributed Cache

**Goal:** shared low-latency cache.

## Key ideas

- Consistent hashing with virtual nodes; replication for availability
- Cache-aside/write-through strategies; TTL and eviction policies
- Hot-key mitigation via local caches and key splitting
- Invalidation via pub/sub and versioned keys

## Interview checklist

- Clarify functional and non-functional requirements and scale.
- Sketch the API and data model before components.
- Back-of-the-envelope capacity (QPS, storage, bandwidth).
- Identify bottlenecks, consistency needs, and failure modes.
- Finish with trade-offs and what you would monitor.
