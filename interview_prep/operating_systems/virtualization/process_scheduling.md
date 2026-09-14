# Process Scheduling

## Workload assumptions

Jobs arrive at once, run for a known time, use the CPU only, and have a
completion time. Relax each assumption to reach real systems.

## Policies

- **FIFO:** simple, suffers the convoy effect.
- **SJF / STCF:** optimal turnaround when runtimes are known.
- **Round Robin:** fair response time, quantum trade-off.
- **MLFQ:** multiple priority queues, dynamic priority based on behavior.
- **Lottery / stride:** proportional-share scheduling.
- **CFS (Linux):** virtual runtime with a red-black tree.
- **Real-time:** rate-monotonic and earliest-deadline-first.

## Trade-offs

- Turnaround vs response time.
- Fairness vs throughput.
- Predictability vs utilization.
- Overhead of context switches and cache effects.
