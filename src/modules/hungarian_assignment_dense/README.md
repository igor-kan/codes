# Jonker-Volgenant / Kuhn-Munkres O(N^3) Assignment Solver (`hungarian_assignment_dense`)

> Category: **Combinatorial Optimization** | Language: **C++20**

## Overview

Computes exact minimum-cost row-to-column bipartite matching via dual potential reduction and shortest augmenting path slack relaxation.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N^2 * M) shortest augmenting paths with dual potentials` |
| **Space Complexity** | `O(N + M)` |

## Mathematical & Safety Invariants

- Assigned column indices are pairwise distinct across all rows.
- Dual row+col potentials satisfy u[i] + v[j] <= cost[i][j] for every entry.

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
