# Design: Food Delivery

**Goal:** order, dispatch, and tracking.

## Key ideas

- Restaurant catalog and availability; cart and pricing
- Dispatch engine choosing courier by proximity, load, and ETA
- Realtime order tracking via WebSockets/SSE
- Compensation for cancellations and refunds

## Interview checklist

- Clarify functional and non-functional requirements and scale.
- Sketch the API and data model before components.
- Back-of-the-envelope capacity (QPS, storage, bandwidth).
- Identify bottlenecks, consistency needs, and failure modes.
- Finish with trade-offs and what you would monitor.
