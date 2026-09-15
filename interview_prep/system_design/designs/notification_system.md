# Design: Notification System

**Goal:** fan out email/SMS/push reliably.

## Key ideas

- Ingest API -> queue -> per-channel workers with provider adapters
- Template rendering, localization, and user preferences
- Idempotency keys and delivery tracking; retries with backoff
- Rate limiting per provider and suppression lists

## Interview checklist

- Clarify functional and non-functional requirements and scale.
- Sketch the API and data model before components.
- Back-of-the-envelope capacity (QPS, storage, bandwidth).
- Identify bottlenecks, consistency needs, and failure modes.
- Finish with trade-offs and what you would monitor.
