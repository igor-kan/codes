# Resilience Patterns

Keep a system responsive and available in the face of failure and overload.

| Pattern | File | Idea |
|:---|:---|:---|
| Timeout | `timeout.py` | bound the wait |
| Hedge | `hedge.py` | issue redundant requests |
| Fail Fast | `fail_fast.py` | reject immediately when unhealthy |
| Fallback | `fallback.py` | degrade gracefully |
| Load Shedding | `load_shedding.py` | drop work under overload |
| Backpressure | `backpressure.py` | signal upstream to slow down |
| Throttling | `throttling.py` | limit request rate |
| Chaos Engineering | `chaos_engineering.md` | proactively inject failure |

Related: `../cloud_patterns/` (circuit breaker, bulkhead, retry).
