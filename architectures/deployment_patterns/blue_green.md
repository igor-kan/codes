# Blue/Green Deployment

Run two identical environments (blue = live, green = new). After verifying green,
switch traffic atomically; keep blue for instant rollback.

## Pros

- Near-zero downtime and fast rollback.
- Full pre-production validation with production-like load.

## Cons

- Double infrastructure cost during switch.
- Stateful systems need migrations that work with both versions.

Related: Canary, Rolling Update.
