# Gateway Offloading

Move shared, cross-cutting capabilities from every service into the API
gateway: TLS termination, authentication, rate limiting, request validation,
compression, CORS, and response caching.

```
client --> [ gateway: authn, rate limit, TLS, cache ] --> service
```

**Benefits:** services stay focused on domain logic; consistent policy across
the fleet; fewer duplicated libraries.

**Trade-offs:** the gateway can become a central bottleneck and a single point
of failure; keep it stateless and horizontally scalable, and avoid embedding
domain logic in it.

Related: Backends for Frontends, Sidecar, Ambassador, API Gateway.
