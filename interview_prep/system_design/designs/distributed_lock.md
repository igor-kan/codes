# Design: Distributed Lock

**Goal:** mutual exclusion across nodes.

## Key ideas

- Consensus-backed locks (etcd/ZooKeeper) with leases and fencing tokens
- Auto-expiry and session heartbeats to avoid orphaned locks
- Single-node Redis locks are unsafe without fencing/Redlock caveats
- Idempotent critical sections and timeouts

## Interview checklist

- Clarify functional and non-functional requirements and scale.
- Sketch the API and data model before components.
- Back-of-the-envelope capacity (QPS, storage, bandwidth).
- Identify bottlenecks, consistency needs, and failure modes.
- Finish with trade-offs and what you would monitor.
