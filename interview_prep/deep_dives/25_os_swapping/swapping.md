# Swapping and Demand Paging

Physical memory is limited; pages not in use are written to swap and reloaded on
demand.

## Demand paging

1. Access to a non-present page faults.
2. Kernel locates the page (swap or file) and finds a free frame.
3. If no free frame, evict a victim (possibly write it back).
4. Update the page table, TLB, and resume.

## Replacement policies

| Policy | Evicts | Notes |
|:---|:---|:---|
| OPT | farthest future use | optimal, unrealizable |
| FIFO | oldest loaded | Belady's anomaly |
| LRU | least recently used | good, costly to track |
| Clock | sweep with a use bit | practical LRU approximation |
| NFU/aging | counters shifted over time | captures frequency |

## Thrashing

When active working sets exceed memory, the system spends its time paging.
Fix by reducing multiprogramming (admission control) or adding memory.

## Page-fault cost

`fault = trap + select victim + writeback (if dirty) + read + table update`.
