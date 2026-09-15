# Rolling Update

Replace instances a few at a time, keeping the service available throughout.

## Controls

- `maxSurge`/`maxUnavailable` (Kubernetes).
- Readiness gates before shifting traffic.
- PreStop hooks for graceful connection draining.

## Considerations

- Versions coexist, so APIs and schemas must be backward compatible.
- Rollback is another rolling update (slower than blue/green).

Related: Blue/Green, Canary, Backward-Compatible Schema Changes.
