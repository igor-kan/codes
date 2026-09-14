# Write Policies

## Write-through vs write-back

- **Write-through:** every write goes to the next level. Simple, always clean,
  but high bandwidth cost.
- **Write-back:** write only the cache; mark the line **dirty** and write back on
  eviction. Less traffic, needs dirty bits and coherence handling.

## Write-allocate vs no-write-allocate

- **Write-allocate:** on a write miss, load the block into cache, then write.
  Pairs well with write-back.
- **No-write-allocate:** write directly to memory. Pairs with write-through.

## Combinations

| Policy pair | Typical use |
|:---|:---|
| Write-back + write-allocate | L1/L2 general purpose |
| Write-through + no-write-allocate | simple caches, I/O |

## Coherence

Multicore caches need coherence protocols (MSI, MESI, MOESI) to keep copies
consistent; stores to shared lines trigger invalidations or updates.

## Durability

Cache hierarchies delay visibility; memory barriers/fences order writes for
lock-free algorithms.
