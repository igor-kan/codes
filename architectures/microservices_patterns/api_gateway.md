# API Gateway

A single entry point that routes requests to internal services and applies
cross-cutting concerns.

## Responsibilities

- Routing and protocol translation (REST ↔ gRPC).
- Authentication/authorization, rate limiting, quotas.
- Request/response transformation and aggregation.
- TLS termination, caching, and observability.

## Trade-offs

- Avoid a distributed monolith or a bottleneck: keep it stateless and thin.
- Consider Backends for Frontends when clients differ widely.

Related: BFF, Service Mesh, Gateway Offloading.
