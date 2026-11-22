# Double-BFS Exact Tree Diameter & Radius Engine (`centroid_tree_dist_d57`)

> Category: **Tree Algorithms** | Language: **C++20**

## Overview

Finds exact longest simple-path diameter and tree center radius across unweighted acyclic connected graphs via two breadth-first sweeps.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(V)` |
| **Space Complexity** | `O(V)` |

## Mathematical & Safety Invariants

- Tree diameter >= radius * 2 - 1 and equals N - 1 on linear paths.

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
