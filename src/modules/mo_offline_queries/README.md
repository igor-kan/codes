# Mo's Square-Root Decomposition Offline Range Query Engine (`mo_offline_queries`)

> Category: **Range Queries** | Language: **C++20**

## Overview

Orders arbitrary [l, r] offline range-distinct queries in Hilbert/sqrt-block serpentine order, updating global frequency tables via O(1) incremental add/remove pointer slides.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O((N + Q) * sqrt(N))` |
| **Space Complexity** | `O(N + Q)` |

## Mathematical & Safety Invariants

- Answers match exact brute-force set-cardinality evaluation for every [l, r] query.
- Every query preserves its original query index despite block-serpentine reordering.

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
