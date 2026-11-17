# Two-Pass Meldable Pairing Heap with O(1) Decrease-Key (`pairing_heap_meldable`)

> Category: **Heaps & Priority Queues** | Language: **C++20**

## Overview

Implements Fredman-Sedgewick pairing heap using arena-allocated child/sibling links supporting handle-indexed O(1) decrease-key and two-pass pairwise sibling merging on pop_min.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(1) insert/meld/decrease-key amortized, O(log N) amortized extract-min` |
| **Space Complexity** | `O(N)` |

## Mathematical & Safety Invariants

- Parent key never exceeds any child key throughout decrease_key and pop_min.
- Sorted output from repeated pop_min matches sorted multiset of inserted values.

## Module Architecture

| File | Lifecycle Role |
| :--- | :--- |
| `types.hpp` | Stage 01 |
| `errors.hpp` | Stage 02 |
| `interface.hpp` | Stage 03 |
| `core.cpp` | Stage 04 |
| `validation.cpp` | Stage 05 |
| `fast_path.cpp` | Stage 06 |
| `concurrent.cpp` | Stage 07 |
| `invariants.cpp` | Stage 08 |
| `unit_tests.cpp` | Stage 09 |
| `property_tests.cpp` | Stage 10 |
| `benchmark.cpp` | Stage 11 |
| `README.md` | Stage 12 |

## Verification & Execution Example

```text
g++ -std=c++20 -O2 -Wall -Wextra -Werror -pthread core.cpp validation.cpp fast_path.cpp concurrent.cpp invariants.cpp unit_tests.cpp -o test_bin && ./test_bin
```

---
© 2026 Igor Kan
