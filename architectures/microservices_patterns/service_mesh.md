# Service Mesh

Move service-to-service networking concerns (mTLS, retries, timeouts, traffic
shifting, telemetry) into a sidecar/data-plane proxy managed by a control plane.

## Components

- **Data plane:** Envoy/proxy per pod, handles traffic.
- **Control plane:** configuration, policy, certificates (Istio, Linkerd).

## Benefits

- Uniform, language-agnostic networking policy.
- Fine-grained traffic control (canary, mirroring) and mTLS by default.

## Costs

- Extra hop latency and resource overhead.
- Operational complexity; start with sidecars only where needed.

Related: Sidecar, Ambassador, Service Discovery.
