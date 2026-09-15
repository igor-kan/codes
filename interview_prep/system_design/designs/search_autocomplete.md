# Design: Search Autocomplete

**Goal:** prefix suggestions under 100 ms at scale.

## Key ideas

- Trie in memory per shard with top-k caches at nodes
- Precompute top queries per prefix offline (MapReduce) into a KV store
- Rank by frequency, recency, and personalization
- Edge cache and CDN for hot prefixes; debounce client input

## Interview checklist

- Clarify functional and non-functional requirements and scale.
- Sketch the API and data model before components.
- Back-of-the-envelope capacity (QPS, storage, bandwidth).
- Identify bottlenecks, consistency needs, and failure modes.
- Finish with trade-offs and what you would monitor.
