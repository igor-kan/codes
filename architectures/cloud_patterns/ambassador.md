# Ambassador Pattern

A specialized sidecar that proxies *outbound* traffic on behalf of the
application, offloading concerns such as retries, circuit breaking, discovery,
TLS, and request logging. The app talks to `localhost`; the ambassador handles
the network.

```
app --> localhost:6379 (ambassador) --> redis.service:6379
```

**Benefits:** language-agnostic networking, consistent policy, centralized
observability. The application stays free of client-side resilience code.

**Trade-offs:** an extra network hop and a component that can become a
bottleneck or single point of failure if misconfigured.

Related: Sidecar, Service Mesh (Istio/Linkerd), Circuit Breaker.
