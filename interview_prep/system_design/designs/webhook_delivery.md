# Design: Webhook Delivery

**Goal:** reliably push events to subscribers.

## Key ideas

- Persistent queue per subscriber; retries with exponential backoff
- Signing payloads (HMAC) and replay protection
- Dead-letter and manual redelivery after failures
- Per-subscriber rate limits and circuit breaking

## Interview checklist

- Clarify functional and non-functional requirements and scale.
- Sketch the API and data model before components.
- Back-of-the-envelope capacity (QPS, storage, bandwidth).
- Identify bottlenecks, consistency needs, and failure modes.
- Finish with trade-offs and what you would monitor.
