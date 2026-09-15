# Design: Ride Hailing Backend

**Goal:** match and track trips.

## Key ideas

- Location ingestion pipeline; geospatial indexing
- Matching and dispatch with ETAs and pricing
- Trip orchestration, payments, and receipts
- Realtime tracking and map data

## Interview checklist

- Clarify functional and non-functional requirements and scale.
- Sketch the API and data model before components.
- Back-of-the-envelope capacity (QPS, storage, bandwidth).
- Identify bottlenecks, consistency needs, and failure modes.
- Finish with trade-offs and what you would monitor.
