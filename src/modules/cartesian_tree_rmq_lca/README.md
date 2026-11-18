# Linear-Time Stack Cartesian Tree & Range Minimum Query (`cartesian_tree_rmq_lca`)

> Category: **Trees & RMQ** | Language: **C++20**

## Overview

Constructs a min-heap Cartesian tree from an array in O(N) time using a monotonic right-spine stack so the LCA of any two indices yields the range minimum index.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N) monotonic right-spine construction + O(H) LCA range minimum` |
| **Space Complexity** | `O(N)` |

## Mathematical & Safety Invariants

- In-order traversal reproduces exact original index order 0..N-1.
- Parent value is <= child value at every tree edge.

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
