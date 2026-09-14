# Design: Social News Feed

## Requirements

- Users follow others and see a ranked timeline.
- Read-heavy; must handle celebrities with millions of followers.
- Freshness matters; ranking balances recency and affinity.

## Fan-out strategies

- **Fan-out on write (push):** precompute each follower's feed at post time.
  Fast reads, expensive for celebrities.
- **Fan-out on read (pull):** build the feed at request time.
  Cheap writes, slower reads and more work per read.
- **Hybrid:** push for normal users, pull for high-follower accounts.

## Architecture

- Feed cache per user (Redis) holding post IDs.
- Post store (sharded KV) for content and metadata.
- Ranking service combines recency, engagement, and affinity.
- Async workers for fan-out, media processing, and notifications.

## Trade-offs

- Celebrity handling, cold-start, and cache size.
- Pagination via cursors; eventual consistency is acceptable.
