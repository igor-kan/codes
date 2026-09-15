# Event Stream

An ordered, partitioned, replayable append-only log consumed by many readers.

## Properties

- Ordering per partition; total order only within a key.
- Durable retention with replay from offsets.
- Consumers track their own position.

## Engineering concerns

- Idempotent consumers and exactly-once sinks.
- Backpressure and consumer lag monitoring.
- Schema registry and compatibility rules.

Related: Kafka, Pulsar, Event Sourcing.
