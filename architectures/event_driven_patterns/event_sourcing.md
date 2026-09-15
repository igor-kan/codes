# Event Sourcing

Persist every state change as an immutable event; current state is a fold over
the log.

## Benefits

- Complete audit trail and temporal queries.
- Enables projections, replay, and new read models.
- Natural fit with CQRS.

## Costs

- Event schema versioning and upcasting.
- Snapshotting is needed for performance.
- Deleting data requires crypto-shredding or tombstones.

Related: CQRS, Event Stream, `../microservices_patterns/event_sourcing.py`.
