# Swapping and Demand Paging

Physical memory is finite; the OS moves pages to disk (swap) and back.

## Demand paging

1. Access faults because the page is not present.
2. Kernel finds the page on swap/disk.
3. Load it into a free frame (possibly evicting another page).
4. Update the page table and resume the instruction.

## Replacement policies

| Policy | Behavior | Notes |
|:---|:---|:---|
| FIFO | evict oldest | suffers Belady's anomaly |
| LRU | evict least recently used | good, expensive to track |
| Clock | approximate LRU with a reference bit | practical |
| OPT | evict farthest in future | theoretical optimum |

## Working set and thrashing

- **Working set:** pages a process actively uses.
- If the sum of working sets exceeds memory, the system **thrashes**.
- Admission control or reducing multiprogramming restores progress.
