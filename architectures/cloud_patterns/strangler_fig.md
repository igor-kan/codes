# Strangler Fig Pattern

Incrementally replace a legacy system by routing functionality to new
services, one slice at a time, until the legacy system can be decommissioned —
like a strangler fig growing around its host tree.

## Steps

1. Introduce a facade/proxy in front of the legacy system.
2. Route one user journey or bounded context to the new implementation.
3. Run legacy and new paths in parallel and compare (shadow traffic).
4. Migrate data incrementally with a bidirectional sync.
5. Repeat until the legacy path is unused, then remove it.

**Benefits:** reduced migration risk, continuous delivery of value, no
big-bang rewrite.

**Risks:** long-lived dual-running cost, data consistency between old and new,
and unclear ownership during the transition.

Related: Anti-Corruption Layer, Branch by Abstraction, Facade.
