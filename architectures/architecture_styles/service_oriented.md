# Service-Oriented Architecture (SOA)

Coarse-grained, reusable services communicating over an enterprise service bus
(ESB).

## Characteristics

- Services expose contracts; the ESB handles routing, transformation, and
  orchestration.
- Emphasis on reuse and enterprise integration.

## Contrast with microservices

- SOA tends to centralize logic in the ESB; microservices push it into services.
- SOA services are often larger and share data stores.

Modern practice favors lightweight integration (APIs, events) over heavyweight
ESBs.

Related: Microservices, Enterprise Integration Patterns.
