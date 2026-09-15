# API Composition

Implement a query that spans services by invoking each service and joining the
results in memory (often in a gateway or BFF).

## When to use

- Simple joins across few services.
- Read-heavy queries where a CQRS read model is overkill.

## Challenges

- Latency of multiple calls; parallelize and cache.
- Partial failures need fallbacks or timeouts.
- In-memory joins are inefficient for large datasets — use a read model instead.

Related: CQRS, BFF, API Gateway.
