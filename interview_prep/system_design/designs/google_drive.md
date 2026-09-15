# Design: File Storage (Drive)

**Goal:** sync files across devices.

## Key ideas

- Block-level chunking with content-addressed dedup
- Metadata service + object storage for blobs
- Sync protocol with change log, conflict resolution, and versions
- Sharing/permissions model and notifications

## Interview checklist

- Clarify functional and non-functional requirements and scale.
- Sketch the API and data model before components.
- Back-of-the-envelope capacity (QPS, storage, bandwidth).
- Identify bottlenecks, consistency needs, and failure modes.
- Finish with trade-offs and what you would monitor.
