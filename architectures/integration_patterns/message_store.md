# Message Store

Persist messages durably so they can be replayed, audited, or delivered after a
consumer outage.

## Implementations

- Append-only logs (Kafka), queue stores (RabbitMQ durable queues),
  transactional outbox tables.
- Object storage for large payloads (claim check).

## Requirements

- Durable writes and crash recovery.
- Ordering and retention policies.
- Idempotent consumers to tolerate redelivery.

## Trade-offs

Storage cost, retention policies vs compliance, and the risk of unbounded
growth. Pair with compaction or TTL.

Related: Claim Check, Guaranteed Delivery, Event Sourcing.
