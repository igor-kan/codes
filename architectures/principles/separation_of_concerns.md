# Separation of Concerns (SoC)

Structure a system so each part addresses a distinct concern, minimizing
overlap. Classic axes:

- **Presentation / Application / Domain / Infrastructure** (layers).
- **Policy vs mechanism:** business rules vs how they are carried out.
- **Read vs write** (CQRS).
- **Configuration vs code.**

## Practical boundaries

| Layer | Knows about | Must not know |
|:---|:---|:---|
| Domain | ubiquitous language, invariants | HTTP, SQL, frameworks |
| Application | use-case orchestration | transport details |
| Infrastructure | databases, queues, APIs | domain invariants |
| Presentation | transport, serialization | persistence |

## Payoff

- Independent testability (domain unit tests need no I/O).
- Independent deployability of parts.
- Replaceable mechanisms (swap Postgres for DynamoDB behind a repository).

**Caution:** too many layers for a small problem is over-engineering. Draw a
boundary only where the rate or reason for change differs.

Related: Clean Architecture, Dependency Inversion, DDD.
