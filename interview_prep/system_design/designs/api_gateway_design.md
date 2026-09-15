# Design: API Gateway

**Goal:** edge routing and policy.

## Key ideas

- Route matching, authN/authZ, and per-key rate limits
- Request/response transformation and aggregation
- Caching, retries, and circuit breaking at the edge
- Observability: access logs, metrics, traces

## Interview checklist

- Clarify functional and non-functional requirements and scale.
- Sketch the API and data model before components.
- Back-of-the-envelope capacity (QPS, storage, bandwidth).
- Identify bottlenecks, consistency needs, and failure modes.
- Finish with trade-offs and what you would monitor.
