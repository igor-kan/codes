# Hilbert Curve Ordering for Low-Movement Offline Range Queries (`mo_tree_hilbert_order`)

> Category: **Offline Query Processing** | Language: **C++20**

## Overview

Maps 2D range query intervals [L, R] to 1D Hilbert space-filling curve positions to minimize two-pointer boundary moves across batches.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O((N + Q) sqrt(N)) Hilbert-curve ordered Mo pointer window` |
| **Space Complexity** | `O(N + Q)` |

## Mathematical & Safety Invariants

- Offline distinct count per query equals exact hash-set distinct count on arr[L..R].

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
