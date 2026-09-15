# Multi-CPU Scheduling

## Design choices

- **Per-CPU run queues** with load balancing, or a single global queue with
  contention.
- **Affinity:** keep a task on the same CPU to preserve cache/TLB warmth.
- **Work stealing:** idle CPUs pull tasks from busy queues.
- **Gang scheduling:** co-schedule related threads (MPI, parallel loops).

## Synchronization

Per-CPU queues avoid a global lock; use atomic counters or sharded locks for
migration decisions.

## NUMA

Memory locality matters: schedule threads near the memory they touch, or migrate
pages along with tasks.

## Scalability issues

- Lock contention on shared run queues.
- Cache-line bouncing on scheduler statistics.
- Load imbalance from bursty or long-running tasks.
- Power/thermal constraints (big.LITTLE, P/E cores).
