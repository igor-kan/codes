# Event-Driven Architecture

Components communicate by producing and consuming events, decoupled in time.

## Topologies

- **Broker (choreography):** no central coordinator; highly decoupled.
- **Mediator (orchestration):** a coordinator drives the flow.

## Benefits

- Loose coupling and extensibility.
- Asynchronous buffering absorbs spikes.

## Challenges

- Eventual consistency and debugging across services.
- Ordering, duplication, and schema evolution.
- Event sprawl without governance.

Related: Event-Driven Patterns, CQRS, Event Sourcing.
