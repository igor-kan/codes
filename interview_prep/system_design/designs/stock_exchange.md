# Design: Stock Exchange

**Goal:** low-latency matching with fairness.

## Key ideas

- Single-threaded matching engine per symbol (deterministic, in-memory)
- Order gateway with sequencing; price-time priority book
- Market data multicast; risk checks before acceptance
- Durability via WAL and replay; colocation for latency

## Interview checklist

- Clarify functional and non-functional requirements and scale.
- Sketch the API and data model before components.
- Back-of-the-envelope capacity (QPS, storage, bandwidth).
- Identify bottlenecks, consistency needs, and failure modes.
- Finish with trade-offs and what you would monitor.
