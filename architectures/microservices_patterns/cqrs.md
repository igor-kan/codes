# Command Query Responsibility Segregation (CQRS)

Separate the write model (commands) from the read model (queries).

```
commands -> write model -> events -> projections -> read model <- queries
```

## Benefits

- Optimize each side independently (normalized writes, denormalized reads).
- Scales reads and writes separately.
- Natural fit with event sourcing.

## Costs

- Eventual consistency between write and read models.
- More moving parts and projection management.
- Complexity is unjustified for simple CRUD.

Related: Event Sourcing, Microservices, Materialized Views.
