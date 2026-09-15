# Design: Hotel Booking

**Goal:** inventory and reservations across properties.

## Key ideas

- Availability calendar per room type with date-range inventory
- Hold + confirm with TTL; overbooking policy
- Search index with pricing and filters; caching
- Consistency per property; eventual consistency for search

## Interview checklist

- Clarify functional and non-functional requirements and scale.
- Sketch the API and data model before components.
- Back-of-the-envelope capacity (QPS, storage, bandwidth).
- Identify bottlenecks, consistency needs, and failure modes.
- Finish with trade-offs and what you would monitor.
