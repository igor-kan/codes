# Design: Local Reviews

**Goal:** search businesses and reviews.

## Key ideas

- Geospatial + text search index over businesses
- Review ingestion with spam/abuse detection
- Ranking by distance, rating, and personalization
- Caching of popular queries and photos on CDN

## Interview checklist

- Clarify functional and non-functional requirements and scale.
- Sketch the API and data model before components.
- Back-of-the-envelope capacity (QPS, storage, bandwidth).
- Identify bottlenecks, consistency needs, and failure modes.
- Finish with trade-offs and what you would monitor.
