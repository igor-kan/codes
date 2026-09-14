# GraphQL vs REST

| Concern | REST | GraphQL |
|:---|:---|:---|
| Endpoint shape | many resource URLs | single `/graphql` endpoint |
| Over/under-fetching | common | client selects exact fields |
| Caching | HTTP caches, CDN | client-side normalized cache (no HTTP CDN) |
| Versioning | URL/media type | schema evolution, deprecate fields |
| File upload | straightforward | multipart/`graphql-upload` |
| Authorization | per route | per field resolver |
| Best for | simple resources, CDN caching, public APIs | rich clients, aggregating many sources |

## Guidelines

- Choose GraphQL when clients have varied, nested data needs and you control
  them; REST when the API is public, cache-heavy, or resource-oriented.
- Guard GraphQL against expensive queries: depth/complexity limits, persisted
  queries, dataloader batching.
- Either way, define pagination, error shapes, and rate limits explicitly.

Related: REST Guidelines, Federation, Pagination, API Governance.
