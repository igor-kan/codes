# Design: Web Crawler

## Requirements

- Crawl billions of pages politely, deduplicate, refresh, extract links.
- Respect robots.txt and rate limits per host.

## Pipeline

```
seed URLs -> URL frontier -> fetcher -> parser -> content store -> link extractor
                                |                         |
                                +-- dedup (Bloom/sha) <---+
```

## Components

- **URL frontier:** priority queues by politeness and importance.
- **Dedup:** Bloom filter plus exact store for URL/content fingerprints.
- **Fetcher:** distributed workers with per-host rate limits, DNS cache.
- **Parser:** extract text/links; handle encodings and redirects.
- **Storage:** raw HTML (object store), extracted text (search index).

## Scale and etiquette

- Distributed by host hash; checkpointing for resumability.
- Exponential backoff on errors; honor `Retry-After`.
- Avoid spider traps (infinite calendars) via depth/pattern limits.
