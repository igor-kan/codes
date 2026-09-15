# Content Delivery Networks

## Purpose

Serve content from caches close to users: lower latency, less origin load,
better resilience against spikes and DDoS.

## Request routing

- **DNS-based:** resolver returns the nearest edge via GeoDNS/anycast.
- **Anycast:** same IP announced from many locations; BGP picks the closest.
- **Request routing:** central scheduler redirects to a selected edge.

## Caching

- **Pull:** edge fetches on miss and caches per `Cache-Control`/`ETag`.
- **Push:** content is proactively uploaded to edges.
- Versioned, immutable assets avoid invalidation.
- **Shield tier** aggregates origin fetches to reduce load.

## Dynamic content

- TLS termination, connection pooling, and request coalescing at the edge.
- Edge compute (workers) for personalization and A/B testing.

## Consistency

Propagation delays mean caches may be momentarily stale; use short TTLs or
purge APIs when correctness demands freshness.
