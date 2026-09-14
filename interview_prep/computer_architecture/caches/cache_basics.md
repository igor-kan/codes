# Cache Basics

Caches exploit **temporal** and **spatial** locality to bridge the CPU-memory
latency gap.

## Terms

- **Hit/miss**, hit rate, miss penalty.
- **Block (line) size**, number of **sets**, **associativity**.
- Address decomposition: tag | index | block offset.
- **AMAT** = hit time + miss rate × miss penalty.

## Placement

| Mapping | Sets a block can go | Conflict misses |
|:---|:---|:---|
| Direct mapped | exactly 1 | many |
| Set associative | N ways | fewer |
| Fully associative | any | none (expensive lookup) |

## Replacement

LRU, pseudo-LRU, random, FIFO, and the theoretical OPT (Belady's).

## Write policies

- **Write-through** vs **write-back**.
- **Write-allocate** vs **no-write-allocate**.
- Dirty bits reduce writebacks.

## The three C's of misses

Compulsory (cold), capacity, conflict.
