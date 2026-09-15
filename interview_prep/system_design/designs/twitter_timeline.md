# Design: Social Timeline

**Goal:** home timeline at scale.

## Key ideas

- Hybrid fan-out: push for most, pull for celebrities
- Per-user timeline cache of post IDs; hydrate from post store
- Ranking by affinity, recency, engagement
- Trending via streaming counters

## Interview checklist

- Clarify functional and non-functional requirements and scale.
- Sketch the API and data model before components.
- Back-of-the-envelope capacity (QPS, storage, bandwidth).
- Identify bottlenecks, consistency needs, and failure modes.
- Finish with trade-offs and what you would monitor.
