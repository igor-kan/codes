# Deadlock: Coffman Conditions

All four must hold simultaneously:

1. **Mutual exclusion** on resources.
2. **Hold and wait** while requesting more.
3. **No preemption** of held resources.
4. **Circular wait** among threads.

## Strategies

- **Prevention:** break a condition (global lock order, try-lock, one lock).
- **Avoidance:** Banker's algorithm with declared maximum claims.
- **Detection/recovery:** wait-for graph cycle detection, abort a victim.
- **Ignore** when rare and recovery is cheap.

## Wait-for graph

Nodes are threads; an edge T1→T2 means T1 waits for a lock held by T2. A cycle
indicates deadlock.

## Related liveness failures

- **Livelock:** threads retry in lockstep.
- **Starvation:** unfair lock keeps a thread waiting.
- **Priority inversion:** low-priority holder blocks high-priority waiter.
