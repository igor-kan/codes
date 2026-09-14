# Sidecar Pattern

Deploy a helper process alongside the application container in the same pod
(or task) so it shares the network namespace and volumes without being part of
the application code. Typical responsibilities: TLS termination, log shipping,
metrics scraping, service-mesh proxying, config reloading.

```yaml
spec:
  containers:
    - name: app
      image: ghcr.io/example/api:1.2.3
    - name: envoy
      image: envoyproxy/envoy:v1.31
      ports: [{ containerPort: 9901 }]
```

**When to use:** cross-cutting concerns owned by the platform rather than the
app, especially when you cannot change application code.

**Trade-offs:** extra resource consumption per pod, more moving parts, and
lifecycle coupling (the sidecar must be ready before the app serves traffic).

Related: Ambassador, Adapter, Service Mesh.
