# Locks

Mutual exclusion primitive: at most one thread in the critical section.

## Requirements

1. Mutual exclusion.
2. Progress (no unnecessary blocking).
3. Bounded waiting (no starvation).

## Hardware primitives

- **Test-and-set:** atomically set and return the old value.
- **Compare-and-swap (CAS):** atomically compare and replace.
- **Load-linked/store-conditional (LL/SC):** RISC alternative.
- **Fetch-and-add:** atomic increment (ticket locks).

## Implementations

| Lock | Fairness | Notes |
|:---|:---|:---|
| Spin | none | burns CPU; good for short sections |
| Ticket | FIFO | simple fair ordering |
| MCS | FIFO | scalable, queue per waiter |
| CLH | FIFO | linked list, good for NUMA |
| Futex | kernel | sleeps instead of spinning |

## Costs

Contention, cache-line ping-pong, priority inversion. Mitigate with backoff,
padding, and lock striping.
