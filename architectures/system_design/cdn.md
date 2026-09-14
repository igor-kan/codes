# Content Delivery Network (CDN)

A geographically distributed cache that serves content from an edge close to
the user, reducing latency and origin load.

## How it works

1. DNS/anycast routes the client to the nearest edge (POP).
2. On a cache miss, the edge fetches from the origin via a shield tier.
3. Responses carry `Cache-Control`/`ETag` headers controlling freshness.
4. Invalidation or versioned URLs update cached objects.

## Caching headers

```http
Cache-Control: public, max-age=31536000, immutable
ETag: "v1-abc123"
Vary: Accept-Encoding
```

## Strategies

- **Push** (upload assets) vs **pull** (lazy fetch from origin).
- **Immutable, versioned assets** (`app.8f3c1.js`) avoid invalidation.
- **Stale-while-revalidate** serves stale content while refreshing.

Related: Cache-Aside, Rate Limiting, Edge Computing.
