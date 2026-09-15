# Mesh Architecture

Push cross-cutting networking into a uniform infrastructure layer (service mesh)
plus API gateway at the edge.

## Layers

- **Edge:** API gateway/BFF handles north-south traffic.
- **Mesh:** sidecars/proxies handle east-west traffic (mTLS, retries, telemetry).
- **Control plane:** policy, identity, and configuration.

## Benefits

- Consistent security and observability without changing services.
- Fine-grained traffic control for progressive delivery.

Related: Service Mesh, API Gateway, Zero Trust.
