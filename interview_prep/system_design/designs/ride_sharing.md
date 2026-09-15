# Design: Ride Sharing

**Goal:** match riders and drivers in real time.

## Key ideas

- Geospatial index (geohash/S2/H3) for nearby-driver queries
- Location updates via streams; in-memory driver state
- Matching service with ETA and pricing; surge multipliers
- Trip state machine, payments, and ratings

## Interview checklist

- Clarify functional and non-functional requirements and scale.
- Sketch the API and data model before components.
- Back-of-the-envelope capacity (QPS, storage, bandwidth).
- Identify bottlenecks, consistency needs, and failure modes.
- Finish with trade-offs and what you would monitor.
