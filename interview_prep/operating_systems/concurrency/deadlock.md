# Deadlock

A set of threads is deadlocked when each waits for a resource held by another.

## Coffman conditions (all must hold)

1. **Mutual exclusion** on resources.
2. **Hold and wait** while acquiring others.
3. **No preemption** of held resources.
4. **Circular wait** among threads.

Break any one to prevent deadlock.

## Strategies

- **Prevention:** global lock ordering, single lock, lock-free structures.
- **Avoidance:** Banker's algorithm with declared maximum needs.
- **Detection & recovery:** wait-for graph cycle detection, abort a victim.
- **Ignore:** acceptable in some systems if deadlock is rare.

## Related liveness problems

- **Livelock:** threads act but make no progress.
- **Starvation:** a thread never acquires a contested resource.
- **Priority inversion:** low-priority holder blocks a high-priority waiter;
  fix with priority inheritance.
