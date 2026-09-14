# Prefetching

Hide memory latency by fetching data before it is explicitly requested.

## Kinds

- **Hardware:** stride detectors, stream buffers, next-line prefetchers.
- **Software:** explicit prefetch instructions or data layout changes.
- **Compiler-directed:** reordering and unrolling to expose access patterns.

## Effectiveness

- Works when access patterns are regular and predictable.
- Can hurt by wasting bandwidth or evicting useful lines (cache pollution).
- Aggressiveness tuned per workload.

## Techniques

- Stride prefetching for loops with constant stride.
- Pointer-chasing prefetch for linked structures.
- Software pipelining to overlap compute and memory.
- Prefetch distance ≈ memory latency / (loop body time).
