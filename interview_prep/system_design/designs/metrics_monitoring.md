# Design: Metrics & Monitoring

**Goal:** collect and query time series.

## Key ideas

- Ingest with batching and backpressure; downsample for retention
- Time-series store with rollups and retention tiers
- Query engine and alerting rule evaluation
- Dashboards and anomaly detection on top

## Interview checklist

- Clarify functional and non-functional requirements and scale.
- Sketch the API and data model before components.
- Back-of-the-envelope capacity (QPS, storage, bandwidth).
- Identify bottlenecks, consistency needs, and failure modes.
- Finish with trade-offs and what you would monitor.
