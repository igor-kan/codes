# Dense O(V^2) Prim Minimum Spanning Tree Solver (`prim_dense_mst_d58`)

> Category: **Spanning Trees** | Language: **C++20**

## Overview

Constructs exact minimum spanning tree total weights across complete/dense adjacency matrices without sorting edge lists cleanly.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(V^2) optimal for dense graphs` |
| **Space Complexity** | `O(V)` |

## Mathematical & Safety Invariants

- Symmetric complete graph MST strictly achieves minimal cut weight across all cuts.

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
