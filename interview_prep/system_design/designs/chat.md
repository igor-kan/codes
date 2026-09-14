# Design: Chat / Messaging

## Requirements

- 1:1 and group messaging, delivery/read receipts, presence, history.
- Ordering per conversation, at-least-once delivery, offline support.
- Millions of concurrent long-lived connections.

## Components

- **Gateway:** holds WebSocket connections; routes to session/state.
- **Message service:** validates, assigns IDs, persists, fans out.
- **Presence service:** heartbeats, status, last-seen.
- **Storage:** messages in a wide-column store keyed by conversation/time.
- **Push:** offline notifications via APNs/FCM.
- **Fan-out:** per-user queues for small groups; write-fan-out for large.

## Delivery

- Per-conversation monotonically increasing sequence numbers.
- Client ACKs; server retries unacked messages.
- Idempotency keys dedupe retries.

## Scale

- Shard connections across gateways; sticky sessions by user.
- Kafka for durable internal transport; consumer groups per shard.
