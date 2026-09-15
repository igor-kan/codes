# Design: Payment System

**Goal:** process payments exactly once with auditability.

## Key ideas

- Ledger with double-entry accounting as source of truth
- Idempotency keys on every charge; state machine per payment
- Outbox for events; reconciliation against provider statements
- PCI scope reduction via tokenization and hosted fields

## Interview checklist

- Clarify functional and non-functional requirements and scale.
- Sketch the API and data model before components.
- Back-of-the-envelope capacity (QPS, storage, bandwidth).
- Identify bottlenecks, consistency needs, and failure modes.
- Finish with trade-offs and what you would monitor.
