# Database per Service

Each service owns its data store; other services access it only through APIs or
events.

## Benefits

- Independent schemas and technology choices.
- Loose coupling and independent deployability.
- Clear data ownership and failure isolation.

## Challenges

- Cross-service queries need API composition or CQRS read models.
- Distributed transactions require sagas.
- Duplication and eventual consistency must be designed for.

## Anti-pattern

A **shared database** couples services through schemas and locks, defeating the
architecture's independence.

Related: Saga, CQRS, Event Sourcing, API Composition.
