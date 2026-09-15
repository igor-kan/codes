# Backends for Frontends (BFF)

One backend per client type (web, mobile, TV) that tailors the API and
aggregates downstream services.

## Why

- Mobile needs smaller payloads and fewer round trips than web.
- Decouples client evolution from service evolution.
- Centralizes client-specific auth and orchestration.

## Trade-offs

- More deployables to own.
- Risk of duplicated logic; share via libraries or a gateway.

Related: API Gateway, API Composition, GraphQL.
