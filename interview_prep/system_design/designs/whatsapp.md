# Design: Chat System

**Goal:** 1:1 and group messaging.

## Key ideas

- WebSocket gateways with sticky sessions; session registry
- Per-conversation sequencing; at-least-once with client ACKs
- Store-and-forward for offline users; push notifications
- Group fan-out and E2E encryption key management

## Interview checklist

- Clarify functional and non-functional requirements and scale.
- Sketch the API and data model before components.
- Back-of-the-envelope capacity (QPS, storage, bandwidth).
- Identify bottlenecks, consistency needs, and failure modes.
- Finish with trade-offs and what you would monitor.
