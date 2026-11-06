# Memory Hierarchy & Cacheline Alignment Standards: codes

Modern high-performance execution is fundamentally bounded by memory bandwidth and latency rather than arithmetic capacity. This specification establishes our cacheline alignment and footprint budgets.

## Hardware Latency Reference Matrix

| Storage Level | Typical Latency (Cycles) | Cacheline Size | Alignment Target |
| :--- | :--- | :--- | :--- |
| **L1 Data Cache** | ~4 - 5 cycles | 64 Bytes | 64-byte aligned |
| **L2 Unified Cache** | ~12 - 14 cycles | 64 Bytes | 64-byte aligned |
| **L3 Shared Cache** | ~35 - 50 cycles | 64 Bytes | 64-byte aligned |
| **Main Memory (DRAM)**| ~150 - 250 cycles | Pages (4 KiB / 2 MiB) | Page-aligned for I/O |

## Cache Alignment Rules

1. **Structure Layout**: All structs frequently accessed in tight loops must have their fields ordered by decreasing alignment size to avoid internal padding holes.
2. **False Sharing Elimination**: Data structures accessed concurrently by multiple threads must use 64-byte padding between per-thread states to prevent L1/L2 cacheline thrashing.
3. **Vector Alignment**: Buffers designated for SIMD instructions (AVX2/AVX-512) must be allocated on 32-byte or 64-byte aligned boundaries.
