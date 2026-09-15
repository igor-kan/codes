# Design: Proximity Service

**Goal:** find nearby places fast.

## Key ideas

- Geohash/S2 cells with per-cell place indexes
- Search adjacent cells to handle boundary cases
- Cache popular areas; update index from place events
- Rank by distance, rating, and open-now

## Interview checklist

- Clarify functional and non-functional requirements and scale.
- Sketch the API and data model before components.
- Back-of-the-envelope capacity (QPS, storage, bandwidth).
- Identify bottlenecks, consistency needs, and failure modes.
- Finish with trade-offs and what you would monitor.
