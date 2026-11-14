# Hardware Vector Pipeline & Register Allocation: codes

## Architectural Design

This specification establishes register allocation guidelines and hardware instruction pipelining standards across `codes`.

### 1. Vector Register Budgets

| Target Architecture | Register File | Max Concurrent Accumulators | Unroll Factor |
| :--- | :--- | :--- | :--- |
| **x86_64 AVX2** | YMM0 - YMM15 | 8 accumulators | 4x |
| **x86_64 AVX-512** | ZMM0 - ZMM31 | 16 accumulators | 8x |
| **ARM AArch64** | V0 - V31 (Neon) | 8 accumulators | 4x |

### 2. Instruction Latency Hiding

- FMA instructions require a 4-cycle pipeline latency.
- Unrolling loops across multiple independent accumulator registers hides port latency and prevents pipeline stalls.
- Data prefetching (`_mm_prefetch`) is deployed 2 iterations ahead of computation to eliminate DRAM access latency.
