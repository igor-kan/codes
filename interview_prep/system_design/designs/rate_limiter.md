# Design: Distributed Rate Limiter

## Requirements

- Limit requests per client/API key across a fleet of servers.
- Low latency, high availability, accurate within a tolerance.
- Multiple scopes (user, IP, endpoint) and policies.

## Algorithms

| Algorithm | Bursts | Memory | Notes |
|:---|:---|:---|:---|
| Token bucket | yes | O(1)/key | smooth with burst allowance |
| Leaky bucket | no | queue | constant outflow |
| Fixed window | edge bursts | O(1)/key | simple, boundary spikes |
| Sliding log | exact | O(requests) | expensive |
| Sliding window counter | good | O(1)/key | interpolation of two windows |

## Distributed enforcement

- Central Redis with atomic Lua script; `INCR` + `EXPIRE`.
- Local token bucket with periodic sync (approximate, resilient).
- Per-node rate = global / nodes with gossip for fairness.

## Failure behavior

- **Fail-open** (allow) preserves availability; **fail-closed** protects
  backends. Choose per risk; return `429` with `Retry-After`.
