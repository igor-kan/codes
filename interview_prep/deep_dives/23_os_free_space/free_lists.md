# Free-Space Management

The allocator tracks free regions and satisfies variable-size requests.

## Operations

- `malloc(size)`: find a free block, possibly split it.
- `free(ptr)`: return the block, coalescing with neighbours.

## Placement policies

| Policy | Rule | Strength |
|:---|:---|:---|
| First fit | first block large enough | fast |
| Best fit | smallest sufficient block | less waste, slower |
| Worst fit | largest block | leaves large remainder |

## Splitting and coalescing

- Split when a block is larger than requested.
- Coalesce adjacent free blocks to fight fragmentation.
- Store a header with size and a magic for validation.

## Fragmentation

- **Internal:** wasted space inside an allocated block.
- **External:** many small free holes that cannot satisfy a large request.

## Real allocators

Segregated free lists by size class, slab allocators, buddy systems, and
size-classed caching (tcmalloc, jemalloc).
