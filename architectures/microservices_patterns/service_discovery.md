# Service Discovery

Locate healthy instances of a service dynamically as they scale and move.

## Approaches

- **Client-side:** clients query a registry and load-balance themselves.
- **Server-side:** a load balancer/router resolves and proxies.

## Registries

Consul, etcd, ZooKeeper, Kubernetes Services/DNS, AWS Cloud Map.

## Health and lifecycle

- Registration on startup, deregistration on shutdown.
- Health checks remove unhealthy instances.
- DNS TTLs and caching affect failover speed.

Related: Service Mesh, Load Balancing, Health Checks.
