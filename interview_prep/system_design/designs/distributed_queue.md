# Design: Distributed Message Queue

## Requirements

- Durable publish/subscribe with consumer groups and ordering per partition.
- At-least-once delivery; exactly-once with idempotent consumers.
- High throughput, replay, and retention.

## Log-based design (Kafka-style)

- Topics split into partitions; each partition is an append-only log.
- Producers append; brokers persist segments; consumers track offsets.
- Ordering guaranteed within a partition; keys choose the partition.

## Delivery semantics

- Producer acks: `acks=0/1/all`; idempotent producer with sequence numbers.
- Consumer offsets committed after processing; replay by seeking.
- Transactions for read-process-write exactly-once within Kafka.

## Scale and reliability

- Replication factor with ISR (in-sync replicas); leader election on failure.
- Tiered storage offloads old segments.
- Backpressure via quotas and consumer lag monitoring.

## Alternatives

RabbitMQ (routing, per-message acks), SQS (managed), NATS (lightweight), Pulsar
(compute/storage separation).
