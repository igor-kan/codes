# Message Channel

A logical pipe connecting producers to consumers; decouples them in time and
space.

## Variants

- **Point-to-point:** one consumer per message (work queue).
- **Publish-subscribe:** each subscriber receives a copy (topic).
- **Datatype channel:** separate channel per message type.
- **Invalid message channel / dead letter channel:** park bad messages.
- **Guaranteed delivery:** store-and-forward with acknowledgements.

## Considerations

Ordering (per-partition), backpressure, retention, and delivery semantics
(at-least-once vs exactly-once with idempotency).

Related: Publish/Subscribe, Competing Consumers, Dead Letter Channel.
