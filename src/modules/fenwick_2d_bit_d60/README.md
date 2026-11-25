# Two-Dimensional Fenwick Binary Indexed Tree for Rectangle Prefix Sums (`fenwick_2d_bit_d60`)

> Category: **Range Queries** | Language: **C++20**

## Overview

Supports dynamic additive point updates on a 2D integer grid and inclusion-exclusion rectangle sum queries in double logarithmic time.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(log R * log C) point update and submatrix sum` |
| **Space Complexity** | `O(R * C)` |

## Mathematical & Safety Invariants

- Submatrix sums match direct scalar summation after any sequence of updates.

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
