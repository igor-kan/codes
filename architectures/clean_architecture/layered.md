# Layered Architecture

Organize code into horizontal layers, each depending only on layers beneath it.

| Layer | Responsibility | Example |
|:---|:---|:---|
| Presentation | transport, serialization, validation | REST controllers, gRPC handlers |
| Application | use-case orchestration, transactions | `RegisterUser`, `PlaceOrder` |
| Domain | business rules and invariants | entities, value objects, services |
| Infrastructure | technical mechanisms | repositories, clients, queues |

## Rules

1. Dependencies point **downward** only.
2. A layer may not be skipped arbitrarily (strict layering) unless justified.
3. Cross-cutting concerns (logging, auth, metrics) use middleware/aspects.

## Pitfalls

- **Sinkhole anti-pattern:** layers that only forward calls add cost without value.
- **Leaky abstraction:** exposing ORM entities or HTTP types deep in the domain.

Related: Clean Architecture, Hexagonal, Separation of Concerns.
