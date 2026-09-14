# NUMA and CPU Affinity

## NUMA

Non-uniform memory access: each socket has local memory; remote memory access
costs more latency and bandwidth. Systems expose NUMA nodes and distances.

## Implications

- Allocate memory on the node where it will be used (first-touch policy).
- Pin threads to cores near their data.
- Shard data structures per node to avoid cross-node contention.
- Use huge pages to reduce TLB pressure.

## Tools

- Linux: `numactl`, `taskset`, `/sys/devices/system/node`.
- `mbind`, `set_mempolicy`, `sched_setaffinity`.
- Libraries: jemalloc/tcmalloc numa-aware arenas.

## CPU affinity

- Pin latency-sensitive threads to dedicated cores.
- Isolate cores from the scheduler (`isolcpus`, cgroups).
- Watch out for hyperthread siblings sharing execution units.

## Trade-offs

- Static pinning reduces flexibility; load imbalance hurts.
- Over-subscription can starve other work.
