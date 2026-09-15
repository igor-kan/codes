# Huge Pages

Larger page sizes (2 MB, 1 GB on x86-64) reduce TLB pressure and page-table
size at the cost of internal fragmentation.

## Benefits

- One TLB entry covers 2 MB instead of 4 KB → far fewer TLB misses.
- Smaller, shallower page tables.
- Better for large, contiguous working sets (databases, HPC, VMs).

## Costs

- Internal fragmentation when the working set is small.
- Allocation requires contiguous physical memory; can be slow or fail.
- Overcommit and migration are harder.

## Linux interfaces

- **THP (transparent huge pages):** automatic, `madvise`/`always`.
- **hugetlbfs:** explicit reserved pools, deterministic latency.
- `mmap` with `MAP_HUGETLB`, or `madvise(MADV_HUGEPAGE)`.

## Monitoring

`/proc/meminfo` (`AnonHugePages`, `HugePages_*`), `perf` TLB events.
