# Memory Hierarchy

## Hierarchy

| Level | Typical latency | Typical size |
|:---|:---|:---|
| Registers | < 1 ns | hundreds of bytes |
| L1 cache | ~1 ns | 32-64 KB |
| L2 cache | ~4 ns | 256 KB - 1 MB |
| L3 cache | ~15 ns | 8-64 MB |
| DRAM | ~80 ns | GBs |
| SSD | ~100 µs | TBs |
| Disk | ~10 ms | TBs |

## Locality

- **Temporal:** reuse of the same data.
- **Spatial:** use of nearby data (cache lines, prefetching).

## Design trade-offs

- Block size: larger blocks exploit spatial locality but waste bandwidth.
- Associativity: fewer conflict misses, costlier lookup.
- Replacement and prefetching affect effective latency.

## Amdahl's law and the memory wall

CPU speed grew faster than memory for decades; caches, prefetching and NUMA-aware
placement mitigate the gap.
