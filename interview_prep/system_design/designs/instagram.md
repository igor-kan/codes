# Design: Photo Sharing

**Goal:** upload, feed, and media delivery.

## Key ideas

- Media service stores originals; CDN serves derivatives
- Feed generation via fan-out with hybrid push/pull
- Social graph store; likes/comments as counters
- Trending and exploration services

## Interview checklist

- Clarify functional and non-functional requirements and scale.
- Sketch the API and data model before components.
- Back-of-the-envelope capacity (QPS, storage, bandwidth).
- Identify bottlenecks, consistency needs, and failure modes.
- Finish with trade-offs and what you would monitor.
