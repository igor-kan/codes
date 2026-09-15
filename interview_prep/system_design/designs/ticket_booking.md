# Design: Ticket Booking

**Goal:** seat reservation without double-selling.

## Key ideas

- Hold seats with a short-TTL reservation, then confirm or expire
- Optimistic or row-level locking on seat rows; strong consistency per show
- Queueing/virtual waiting room for hot events
- Idempotent checkout and compensation on payment failure

## Interview checklist

- Clarify functional and non-functional requirements and scale.
- Sketch the API and data model before components.
- Back-of-the-envelope capacity (QPS, storage, bandwidth).
- Identify bottlenecks, consistency needs, and failure modes.
- Finish with trade-offs and what you would monitor.
