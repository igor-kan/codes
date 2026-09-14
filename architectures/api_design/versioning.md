# API Versioning

## Strategies

| Strategy | Example | Notes |
|:---|:---|:---|
| URI path | `/v2/orders` | simplest, most visible; cache-friendly |
| Query param | `/orders?version=2` | easy to add, easy to forget |
| Media type | `Accept: application/vnd.api+json;version=2` | purist; harder to debug |
| Header | `X-API-Version: 2` | clean URLs, less discoverable |

## Compatibility rules

- **Additive** changes (new optional field, new endpoint) are backward
  compatible; release continuously.
- **Breaking** changes (rename/remove field, type change, semantics change)
  require a new major version.
- Tolerant reader: clients ignore unknown fields; servers ignore unknown query
  params where safe.

## Lifecycle

1. Announce with a deprecation window and communicate via `Deprecation` and
   `Sunset` headers.
2. Support at most two live major versions concurrently.
3. Monitor usage per version; remove only when traffic is zero.
4. Document diffs and provide migration guides.

Related: REST Guidelines, Semantic Versioning, API Governance.
