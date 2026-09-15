# Design: Ad Click Aggregator

**Goal:** count clicks at scale with dedup.

## Key ideas

- Click events to a log; idempotent processing by click id
- Stream aggregation with windowing; late-event handling
- Fast read store for dashboards; batch reconciliation
- Fraud filtering and bot detection

## Interview checklist

- Clarify functional and non-functional requirements and scale.
- Sketch the API and data model before components.
- Back-of-the-envelope capacity (QPS, storage, bandwidth).
- Identify bottlenecks, consistency needs, and failure modes.
- Finish with trade-offs and what you would monitor.
