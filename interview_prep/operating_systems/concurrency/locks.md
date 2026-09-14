# Locks

A lock provides mutual exclusion: at most one thread holds it at a time.

## Requirements

1. **Mutual exclusion.**
2. **Progress:** a thread outside the critical section cannot block others.
3. **Bounded waiting:** no starvation.

## Implementations

- **Spin lock:** busy-waits; good when critical sections are tiny.
- **Test-and-set / compare-and-swap:** atomic primitives.
- **Ticket lock:** FIFO fairness via a ticket and turn.
- **MCS lock:** scalable queue-based lock.
- **Futex:** kernel-assisted blocking lock (Linux).

## Costs

- Contention serializes execution.
- Cache-line bouncing between cores.
- Priority inversion (mitigate with priority inheritance).
