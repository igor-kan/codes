# Design: URL Shortener

## Requirements

- Given a long URL, return a short key; resolve a key back to the long URL.
- Read-heavy (100:1), low latency, high availability.
- Optional analytics and custom aliases; expire after a TTL.

## API

```
POST /urls        { "longUrl": "..." } -> { "key": "abc123", "shortUrl": "..." }
GET  /{key}       302 redirect
GET  /urls/{key}  metadata
```

## Key generation

- **Counter + base62:** monotonic, no collisions; needs a distributed counter
  (Snowflake-like) or per-range allocation.
- **Hash (MD5/SHA) + base62 prefix:** handle collisions by retry.
- Avoid random keys causing collisions at scale.

## Storage

- Key-value store: `key -> {longUrl, owner, createdAt, expiresAt}`.
- Cache hot keys in Redis; longer TTL for popular links.
- Shard by key hash; replication for availability.

## Scale

- CDN/cache for redirects; 302 vs 301 trade-off (analytics vs caching).
- Analytics via async stream processing; sweep expired keys in the background.

## Trade-offs

- Deterministic keys leak volume; counter sharding adds complexity.
