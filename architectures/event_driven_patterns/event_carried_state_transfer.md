# Event-Carried State Transfer

The event contains the full state needed by consumers, so they need not call the
source.

## Pros

- Consumers stay available if the source is down.
- Fewer synchronous calls; faster processing.

## Cons

- Larger events; possible stale data.
- Schema evolution and PII handling become important.

Related: Event Notification, Event Sourcing.
